
(function() {
        
            function getPageContext() {
                return Zenoss.env.device_uid || Zenoss.env.PARENT_CONTEXT;
            }
        
            Ext.ComponentMgr.onAvailable('component-add-menu', function(config) {
                var menuButton = Ext.getCmp('component-add-menu');
                menuButton.menuItems.push({
                    xtype: 'menuitem',
                    text: _t('Add Airbiquity Trunk') + '...',
                    hidden: Zenoss.Security.doesNotHavePermission('Manage Device'),
                    handler: function() {
                        var win = new Zenoss.dialog.CloseDialog({
                            width: 300,
                            title: _t('Add Airbiquity Trunk'),
                            items: [{
                                xtype: 'form',
                                buttonAlign: 'left',
                                monitorValid: true,
                                labelAlign: 'top',
                                footerStyle: 'padding-left: 0',
                                border: false,
                                items:                         [
                            {
                                fieldLabel: 'Trunk ID', 
                                allowBlank: 'false', 
                                name: 'trunkID', 
                                width: 260, 
                                id: 'trunkIDField', 
                                xtype: 'textfield'
                            }
                        ]

                                ,
                                buttons: [{
                                    xtype: 'DialogButton',
                                    id: 'AirbiquityDevice-submit',
                                    text: _t('Add'),
                                    formBind: true,
                                    handler: function(b) {
                                        var form = b.ownerCt.ownerCt.getForm();
                                        var opts = form.getFieldValues();
                                        Zenoss.remote.AirbiquityDeviceRouter.addAirbiquityTrunkRouter(opts,
                                        function(response) {
                                            if (response.success) {
                                                new Zenoss.dialog.SimpleMessageDialog({
                                                    title: _t('Airbiquity Trunk Added'),
                                                    message: response.msg,
                                                    buttons: [{
                                                        xtype: 'DialogButton',
                                                        text: _t('OK'),
                                                        handler: function() { 
                                                            window.top.location.reload();
                                                            }
                                                        }]
                                                }).show();
                                            }
                                            else {
                                                new Zenoss.dialog.SimpleMessageDialog({
                                                    message: response.msg,
                                                    buttons: [{
                                                        xtype: 'DialogButton',
                                                        text: _t('OK'),
                                                        handler: function() { 
                                                            window.top.location.reload();
                                                            }
                                                        }]
                                                }).show();
                                            }
                                        });
                                    }
                                }, Zenoss.dialog.CANCEL]
                            }]
                        });
                        win.show();
                    }
                });
            });
        }()
);


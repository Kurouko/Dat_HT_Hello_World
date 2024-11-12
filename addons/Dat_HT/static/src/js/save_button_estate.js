odoo.define('my_module.save_files_button', function (require) {
    "use strict";

    var FormView = require('web.FormView');
    var core = require('web.core');
    var _t = core._t;

    FormView.include({
        events: {
            'click button[name="save_files"]': '_onSaveFilesButtonClick',
        },

        _onSaveFilesButtonClick: function (event) {
            var self = this;
            event.preventDefault();

            // Lấy ID của record đang được xử lý
            var recordId = this.model.get('id');

            // Gọi phương thức Python save_files
            this._rpc({
                model: 'estate.odoo',
                method: 'save_files',
                args: [recordId],  // Pass the record's ID as an argument
            }).then(function (result) {
                self.do_notify(_t("Success"), _t("Tệp đã được lưu thành công."));
            }).catch(function (error) {
                self.do_notify(_t("Error"), _t("Đã xảy ra lỗi khi lưu tệp."));
            });
        },
    });
});

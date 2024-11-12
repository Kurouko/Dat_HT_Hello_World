// static/src/js/show_submit_button.js
odoo.define('Dat_HT.show_submit_button', function (require) {
    "use strict";

    var publicWidget = require('web.public.widget');

    publicWidget.registry.ShowSubmitButton = publicWidget.Widget.extend({
        selector: '.attachment-field',
        events: {
            'change': '_onAttachmentChange',
        },

        _onAttachmentChange: function () {
            // Hiển thị nút khi có file đính kèm
            document.getElementById('submit_button').classList.remove('d-none');
        },
    });
});

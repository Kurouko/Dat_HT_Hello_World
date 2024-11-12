odoo.define('my_module.dynamic_visibility', function (require) {
    "use strict";

    var FormController = require('web.FormController');
    var { Component } = require('owl');

    FormController.include({
        async _onSave() {
            // Example of controlling the visibility based on a condition
            const estate = this.model.get(this.handle);
            if (estate.estate_ids && estate.estate_ids.length > 0) {
                this.el.querySelector('.oe_chatter[data-field="estate_ids"]').style.display = 'block';
            } else {
                this.el.querySelector('.oe_chatter[data-field="estate_ids"]').style.display = 'none';
            }
            return this._super(...arguments);
        },
    });
});

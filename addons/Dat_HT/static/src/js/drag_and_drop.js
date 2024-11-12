odoo.define('Dat_HT.drag_drop', function (require) {
    'use strict';

    var core = require('web.core');
    var Widget = require('web.Widget');
    var FieldBinaryFile = require('web.basic_fields').FieldBinaryFile;
    var _t = core._t;

    // Extend FieldBinaryFile to support drag-and-drop
    var DragDropFieldBinaryFile = FieldBinaryFile.extend({
        events: _.extend({}, FieldBinaryFile.prototype.events, {
            'dragover': '_onDragOver',
            'drop': '_onDrop',
        }),

        // On dragover, prevent default behavior to allow drop
        _onDragOver: function (event) {
            event.preventDefault();
            event.stopPropagation();
            $(event.currentTarget).addClass('drag-over');
        },

        // On drop, process the dropped file
        _onDrop: function (event) {
            event.preventDefault();
            event.stopPropagation();
            $(event.currentTarget).removeClass('drag-over');

            // Get the dropped files
            var files = event.originalEvent.dataTransfer.files;
            if (files && files.length > 0) {
                var file = files[0];  // Assuming single file drop

                // Create a new FileReader to read the dropped file
                var reader = new FileReader();
                reader.onload = (function (theFile) {
                    return function (e) {
                        // Upload the file as base64 data (You can customize this to upload via an API)
                        var attachment = {
                            type: 'binary',
                            filename: theFile.name,
                            mimetype: theFile.type,
                            datas: e.target.result.split(',')[1], // Convert base64 to the correct part
                        };
                        // Trigger the file to be uploaded into the many2many_binary field
                        var field = this.$el.closest('.o_field_widget').data('field');
                        this._setValue([attachment]);

                        // Call the function to add the file to the model
                        this.trigger_up('change', {value: this.value});
                    };
                })(file);
                reader.readAsDataURL(file); // Read file as base64
            }
        },
    });

    // Register the custom drag-and-drop field
    core.form_widget_registry.add('many2many_binary', DragDropFieldBinaryFile);
});

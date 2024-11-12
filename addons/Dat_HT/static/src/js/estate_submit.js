/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

class EstateSubmitButton extends Component {
    setup() {
        this.rpc = useService("rpc");
    }

    async submitEstate() {
        const inputText = document.getElementById("estate_input").value;
        if (inputText) {
            // Gửi dữ liệu đến phương thức Python qua RPC
            await this.rpc({
                model: 'your.model',  // Thay 'your.model' bằng tên model của bạn
                method: 'submit_estate_data',
                args: [inputText],
            });
            // Reset input sau khi submit
            document.getElementById("estate_input").value = "";
        } else {
            alert("Vui lòng nhập thông tin trước khi submit.");
        }
    }
}

EstateSubmitButton.template = xml`
    <div>
        <input type="text" t-att-id="estate_input"/>
        <button t-on-click="submitEstate" class="btn btn-primary">Submit</button>
    </div>
`;

registry.category("actions").add("EstateSubmitButton", EstateSubmitButton);
export default EstateSubmitButton;

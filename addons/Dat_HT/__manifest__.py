{
    # Tên module
    'name': 'Real_Estate_Management_Tools',
    'version': '1.0',

    # Loại module
    'category': 'Tutorial',

    # Độ ưu tiên module trong list module
    # Số càng nhỏ, độ ưu tiên càng cao
    #### Chấp nhận số âm
    'sequence': 5,

    # Mô tả module
    'summary': 'Module này để quản lý các bất động sản',
    'description': '',


    # Module dựa trên các category nào
    # Khi hoạt động, category trong 'depends' phải được install
    ### rồi module này mới đc install
    'depends': [
        'mail',
        'product',
        'point_of_sale',
        'base',
    ],

    # Module có được phép install hay không
    # Nếu bạn thắc mắc nếu tắt thì làm sao để install
    # Bạn có thể dùng 'auto_install'
    'installable': True,
    'auto_install': False,
    'application': True,

    # Import các file cấu hình
    # Những file ảnh hưởng trực tiếp đến giao diện (không phải file để chỉnh sửa giao diện)
    ## hoặc hệ thống (file group, phân quyền)
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv', 
        'views/location_list_template.xml',
        'views/menu_item_location.xml',
        'views/menu_item_estate.xml',   
        'views/product_template_enhance_view.xml',           
        'views/menu_view.xml',   
    ],
    'controllers': [
        
    ],

    # Import các file cấu hình (chỉ gọi từ folder 'static')
    # Những file liên quan đến
    ## + các class mà hệ thống sử dụng
    ## + các chỉnh sửa giao diện
    ## + t
    'assets': {
        'point_of_sale._assets_pos': [
            'Dat_HT/static/src/description/icon.png',
            'Dat_HT/static/src/js/drag_and_drop.js',
            'Dat_HT/static/src/scss/drag_and_drop.scss',
            'Dat_HT/static/src/xml/drag_and_drop_templates.xml',
            'Dat_HT/static/src/js/save_button_estate.js',
            'Dat_HT/static/src/js/visibility.js',
            'Dat_HT/static/src/scss/new_fields.scss',
        ],

    },
    'license': 'LGPL-3',
}

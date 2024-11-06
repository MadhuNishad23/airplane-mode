frappe.ui.form.on('Airline', {
    refresh: function(frm) {
        if (frm.doc.website) {
            frm.add_custom_button(('Visit Website'), function() {
                window.open(frm.doc.website, '_blank');
            });
        }
    },

    on_load: function(frm) {
        // Check if the website field is not empty
        if (frm.doc.website) {
            // Add a web link with the text "Visit Official Website"
            frm.add_web_link(('Visit Official Website'), frm.doc.website);
        }
    }
});
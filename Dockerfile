FROM odoo:15.0

# Copy configuration and addons
COPY ./config/odoo.conf /etc/odoo/odoo.conf
COPY ./odoo/module_testing /mnt/extra-addons

# Set the correct permissions if needed
RUN chown -R odoo:odoo /mnt/extra-addons /etc/odoo/odoo.conf

USER odoo
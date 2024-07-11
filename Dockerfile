FROM odoo:15.0

# Install custom dependencies if needed
RUN pip install -r /mnt/extra-addons/requirements.txt

COPY ./config/odoo.conf /etc/odoo/
COPY ./custom_addons /mnt/extra-addons

# Set permissions
RUN chown -R odoo:odoo /mnt/extra-addons

USER odoo

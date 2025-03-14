FROM odoo:17.0

USER root

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy addons
COPY custom-addons/ /mnt/extra-addons

# Copy addons
COPY config/odoo.conf /etc/odoo.conf

# Set the correct permissions if needed (only for addons)
RUN chown -R odoo:odoo /mnt/extra-addons /etc/odoo.conf
RUN chmod 755 -R /mnt/extra-addons /etc/odoo.conf

USER odoo

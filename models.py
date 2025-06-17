from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 1. Configuración General y Maestros
class Account(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # Ej: Activo, Pasivo, etc.

class BudgetCode(db.Model):
    __tablename__ = 'budget_codes'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)

class Tax(db.Model):
    __tablename__ = 'taxes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    percentage = db.Column(db.Float, nullable=False)
    is_active = db.Column(db.Boolean, default=True)

class CatalogItem(db.Model):
    __tablename__ = 'catalog_items'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)  # 'unidad_medida', 'tipo_documento', etc.
    value = db.Column(db.String(100), nullable=False)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    role = db.Column(db.String(50), nullable=False)  # 'Administrador', 'Comprador', etc.
    password = db.Column(db.String(255), nullable=False)  # Hash

# 2. Compras y Proveedores
class Vendor(db.Model):
    __tablename__ = 'vendors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    tax_id = db.Column(db.String(100))
    contact_info = db.Column(db.String(255))

class PurchaseOrder(db.Model):
    __tablename__ = 'purchase_orders'
    id = db.Column(db.Integer, primary_key=True)
    po_number = db.Column(db.String(50), unique=True, nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=False)
    order_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), default='Open')
    vendor = db.relationship('Vendor', backref='purchase_orders')

class PurchaseOrderItem(db.Model):
    __tablename__ = 'purchase_order_items'
    id = db.Column(db.Integer, primary_key=True)
    po_id = db.Column(db.Integer, db.ForeignKey('purchase_orders.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    description = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    unit_cost = db.Column(db.Float, nullable=False)
    total_cost = db.Column(db.Float, nullable=False)
    budget_code_id = db.Column(db.Integer, db.ForeignKey('budget_codes.id'))
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'))
    po = db.relationship('PurchaseOrder', backref='items')
    item = db.relationship('Item', backref='po_items')
    budget_code = db.relationship('BudgetCode', backref='po_items')
    account = db.relationship('Account', backref='po_items')

class VendorInvoice(db.Model):
    __tablename__ = 'vendor_invoices'
    id = db.Column(db.Integer, primary_key=True)
    invoice_number = db.Column(db.String(50), unique=True, nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=False)
    invoice_date = db.Column(db.Date, nullable=False)
    po_id = db.Column(db.Integer, db.ForeignKey('purchase_orders.id'))
    total_amount = db.Column(db.Float, nullable=False)
    account_payable_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    attachment_id = db.Column(db.Integer, db.ForeignKey('attachments.id'))
    vendor = db.relationship('Vendor', backref='invoices')
    po = db.relationship('PurchaseOrder', backref='invoices')
    account_payable = db.relationship('Account', backref='vendor_invoices')
    attachment = db.relationship('Attachment', backref='vendor_invoices')

class VendorInvoiceItem(db.Model):
    __tablename__ = 'vendor_invoice_items'
    id = db.Column(db.Integer, primary_key=True)
    invoice_id = db.Column(db.Integer, db.ForeignKey('vendor_invoices.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    description = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    unit_cost = db.Column(db.Float, nullable=False)
    total_cost = db.Column(db.Float, nullable=False)
    budget_code_id = db.Column(db.Integer, db.ForeignKey('budget_codes.id'))
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'))
    simulated_inventory_entry_id = db.Column(db.Integer, db.ForeignKey('inventory_entries.id'))
    invoice = db.relationship('VendorInvoice', backref='items')
    item = db.relationship('Item', backref='invoice_items')
    budget_code = db.relationship('BudgetCode', backref='invoice_items')
    account = db.relationship('Account', backref='invoice_items')
    simulated_inventory_entry = db.relationship('InventoryEntry', backref='invoice_items')

# 3. Inventario
class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    unit_id = db.Column(db.Integer, db.ForeignKey('catalog_items.id'))
    cost = db.Column(db.Float, default=0)
    unit = db.relationship('CatalogItem', backref='items')

class InventoryEntry(db.Model):
    __tablename__ = 'inventory_entries'
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    entry_date = db.Column(db.Date, nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    cost_per_unit = db.Column(db.Float, nullable=False)
    source_document_type = db.Column(db.String(50))
    source_document_id = db.Column(db.Integer)
    item = db.relationship('Item', backref='inventory_entries')

# 4. Contabilidad
class JournalEntry(db.Model):
    __tablename__ = 'journal_entries'
    id = db.Column(db.Integer, primary_key=True)
    entry_date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    source_document_type = db.Column(db.String(50))
    source_document_id = db.Column(db.Integer)

class JournalEntryLine(db.Model):
    __tablename__ = 'journal_entry_lines'
    id = db.Column(db.Integer, primary_key=True)
    journal_entry_id = db.Column(db.Integer, db.ForeignKey('journal_entries.id'), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    debit = db.Column(db.Float, default=0)
    credit = db.Column(db.Float, default=0)
    journal_entry = db.relationship('JournalEntry', backref='lines')
    account = db.relationship('Account', backref='journal_entry_lines')

# 5. Presupuesto
class Budget(db.Model):
    __tablename__ = 'budgets'
    id = db.Column(db.Integer, primary_key=True)
    budget_code_id = db.Column(db.Integer, db.ForeignKey('budget_codes.id'), nullable=False)
    period = db.Column(db.String(20), nullable=False)  # Ej: '2025', '2025-Q1'
    amount = db.Column(db.Float, nullable=False)
    budget_code = db.relationship('BudgetCode', backref='budgets')

# 6. Adjuntos
class Attachment(db.Model):
    __tablename__ = 'attachments'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    filepath = db.Column(db.String(255), nullable=False)
    uploaded_at = db.Column(db.DateTime, nullable=False)
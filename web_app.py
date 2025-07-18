from flask import Flask, render_template_string, request, jsonify, redirect, url_for
from sweet_shop import SweetShop
from sweet import Sweet
import json

app = Flask(__name__)
shop = SweetShop("Delight Manager Web Store")

# Load sample data
def load_sample_data():
    sample_sweets = [
        Sweet("Chocolate Bar", "Rich dark chocolate bar", 80, 100, "Chocolate"),
        Sweet("Gummy Bears", "Colorful fruity gummy bears", 10, 75, "Gummy"),
        Sweet("Rainbow Lollipop", "Multi-colored swirl lollipop", 20, 50, "Hard Candy"),
        Sweet("Marshmallows", "Soft fluffy marshmallows", 60, 30, "Soft Candy"),
        Sweet("Chocolate Truffles", "Premium chocolate truffles", 50, 25, "Chocolate"),
        Sweet("Sour Worms", "Tangy sour gummy worms", 75, 60, "Gummy"),
        Sweet("Peppermint Candy", "Classic peppermint hard candy", 20, 80, "Hard Candy"),
        Sweet("Caramel Chews", "Creamy caramel chews", 100, 40, "Soft Candy")
    ]
    
    for sweet in sample_sweets:
        shop.add_sweet(sweet)

load_sample_data()

# HTML Templates
BASE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - Sweet Shop Management</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; background: #f4f4f4; }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 1rem 0; margin-bottom: 2rem; }
        h1 { text-align: center; font-size: 2.5rem; margin-bottom: 0.5rem; }
        .subtitle { text-align: center; opacity: 0.9; }
        nav { background: white; padding: 1rem; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); margin-bottom: 2rem; }
        nav ul { list-style: none; display: flex; flex-wrap: wrap; justify-content: center; gap: 1rem; }
        nav a { text-decoration: none; color: #667eea; padding: 0.5rem 1rem; border-radius: 5px; transition: all 0.3s; }
        nav a:hover { background: #667eea; color: white; }
        .card { background: white; padding: 2rem; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); margin-bottom: 2rem; }
        .sweet-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1rem; }
        .sweet-card { background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); border-left: 4px solid #667eea; }
        .sweet-name { font-size: 1.2rem; font-weight: bold; color: #667eea; margin-bottom: 0.5rem; }
        .sweet-price { font-size: 1.1rem; color: #e74c3c; font-weight: bold; }
        .sweet-category { background: #667eea; color: white; padding: 0.2rem 0.5rem; border-radius: 3px; font-size: 0.8rem; display: inline-block; margin: 0.5rem 0; }
        .form-group { margin-bottom: 1rem; }
        label { display: block; margin-bottom: 0.5rem; font-weight: bold; }
        input, select, textarea { width: 100%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px; font-size: 1rem; }
        button { background: #667eea; color: white; padding: 0.75rem 1.5rem; border: none; border-radius: 4px; cursor: pointer; font-size: 1rem; transition: background 0.3s; }
        button:hover { background: #5a67d8; }
        .btn-danger { background: #e74c3c; }
        .btn-danger:hover { background: #c0392b; }
        .search-bar { display: flex; gap: 1rem; margin-bottom: 2rem; }
        .search-bar input { flex: 1; }
        .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-bottom: 2rem; }
        .stat-card { background: white; padding: 1.5rem; border-radius: 8px; text-align: center; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        .stat-number { font-size: 2rem; font-weight: bold; color: #667eea; }
        .stat-label { color: #666; margin-top: 0.5rem; }
        .alert { padding: 1rem; border-radius: 4px; margin-bottom: 1rem; }
        .alert-success { background: #d4edda; color: #155724; border: 1px solid #c3e6cb; }
        .alert-error { background: #f8d7da; color: #721c24; border: 1px solid #f5c6cb; }
        table { width: 100%; border-collapse: collapse; background: white; }
        th, td { padding: 1rem; text-align: left; border-bottom: 1px solid #ddd; }
        th { background: #f8f9fa; font-weight: bold; }
        .actions { display: flex; gap: 0.5rem; }
        .btn-small { padding: 0.25rem 0.5rem; font-size: 0.8rem; }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>{{ shop_name }}</h1>
            <p class="subtitle">Sweet Shop Management System</p>
        </div>
    </header>
    
    <div class="container">
        <nav>
            <ul>
                <li><a href="/">🏠 Home</a></li>
                <li><a href="/sweets">🍬 All Sweets</a></li>
                <li><a href="/add">➕ Add Sweet</a></li>
                <li><a href="/search">🔍 Search</a></li>
                <li><a href="/categories">📂 Categories</a></li>
                <li><a href="/statistics">📊 Statistics</a></li>
            </ul>
        </nav>
        
        {% block content %}{% endblock %}
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    stats = {
        'total_sweets': len(shop),
        'available_sweets': len(shop.get_available_sweets()),
        'total_value': shop.get_total_value(),
        'categories': len(shop.get_categories()),
        'low_stock': len(shop.get_low_stock_sweets())
    }
    
    recent_sweets = shop.get_all_sweets()[:6]  # Show first 6 sweets
    
    template = BASE_TEMPLATE.replace('{% block content %}{% endblock %}', """
        <div class="card">
            <h2>Welcome to Delight Manager web store</h2>
            <p>Turn your sweet stash into a perfectly managed collection! 🍬✨</p>
        </div>
        
        <div class="stats">
            <div class="stat-card">
                <div class="stat-number">{{ stats.total_sweets }}</div>
                <div class="stat-label">Total Sweets</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{{ stats.available_sweets }}</div>
                <div class="stat-label">Available</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">₹{{ "%.2f"|format(stats.total_value) }}</div>
                <div class="stat-label">Total Value</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{{ stats.categories }}</div>
                <div class="stat-label">Categories</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{{ stats.low_stock }}</div>
                <div class="stat-label">Low Stock</div>
            </div>
        </div>
        
        <div class="card">
            <h3>Featured Sweets</h3>
            <div class="sweet-grid">
                {% for sweet in recent_sweets %}
                <div class="sweet-card">
                  <div class="sweet-id">{{ sweet.id }}</div>
                    <div class="sweet-name">{{ sweet.name }}</div>
                    <div class="sweet-price">₹{{ "%.2f"|format(sweet.price) }}</div>
                    <div class="sweet-category">{{ sweet.category }}</div>
                    <p>{{ sweet.description }}</p>
                    <p><strong>Stock:</strong> {{ sweet.quantity }} available</p>
                </div>
                {% endfor %}
            </div>
        </div>
    """)
    
    return render_template_string(template, 
                                title="Home", 
                                shop_name=shop.name,
                                stats=stats,
                                recent_sweets=recent_sweets)

@app.route('/sweets')
def view_sweets():
    sort_by = request.args.get('sort', 'id')
    order = request.args.get('order', 'asc')
    
    if sort_by == 'price':
        sweets = shop.sort_sweets_by_price(reverse=(order == 'desc'))
    elif sort_by == 'quantity':
        sweets = shop.sort_sweets_by_quantity(reverse=(order == 'desc'))
    elif(sort_by=='name'):
        sweets = shop.sort_sweets_by_name(reverse=(order == 'desc'))
    else:
         sweets = shop.sort_sweets_by_id(reverse=(order == 'desc'))
   
    template = BASE_TEMPLATE.replace('{% block content %}{% endblock %}', """
        <div class="card">
            <h2>All Sweets ({{ sweets|length }})</h2>
            
            <div style="margin-bottom: 1rem;">
                <label>Sort by:</label>
              <select onchange="window.location.href='/sweets?sort=' + this.value + '&order=' + document.getElementById('order').value">
                       <!-- CORRECTED LINE BELOW: value should be "id" -->
                       <option value="id" {{ 'selected' if sort_by == 'id' else '' }}>id</option>
                       <option value="name" {{ 'selected' if sort_by == 'name' else '' }}>Name</option>
                       <option value="price" {{ 'selected' if sort_by == 'price' else '' }}>Price</option>
                       <option value="quantity" {{ 'selected' if sort_by == 'quantity' else '' }}>Quantity</option>
              </select>
                
                <select id="order" onchange="window.location.href='/sweets?sort=' + document.querySelector('select').value + '&order=' + this.value">
                    <option value="asc" {{ 'selected' if order == 'asc' else '' }}>Ascending</option>
                    <option value="desc" {{ 'selected' if order == 'desc' else '' }}>Descending</option>
                </select>
            </div>
            
            <table>
                <thead>
                    <tr>
                        <th>id</th>
                        <th>Name</th>
                        <th>Price</th>
                        <th>Quantity</th>
                        <th>Category</th>
                        <th>Description</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {% for sweet in sweets %}
                    <tr>
                        <td><strong>{{sweet.id}}</strong></td>
                        <td><strong>{{ sweet.name }}</strong></td>
                        <td>₹{{ "%.2f"|format(sweet.price) }}</td>
                        <td>{{ sweet.quantity }}</td>
                        <td><span class="sweet-category">{{ sweet.category }}</span></td>
                        <td>{{ sweet.description }}</td>
                        <td class="actions">
                            <a href="/edit/{{ sweet.name }}" class="btn-small" style="background: #f39c12; color: white; text-decoration: none; padding: 0.25rem 0.5rem; border-radius: 3px;">Edit</a>
                            <a href="/delete/{{ sweet.name }}" class="btn-small btn-danger" style="color: white; text-decoration: none; padding: 0.25rem 0.5rem; border-radius: 3px;" onclick="return confirm('Are you sure?')">Delete</a>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    """)
    
    return render_template_string(template,
                                title="All Sweets",
                                shop_name=shop.name,
                                sweets=sweets,
                                sort_by=sort_by,
                                order=order)

@app.route('/add', methods=['GET', 'POST'])
def add_sweet():
    if request.method == 'POST':
        try:
            name = request.form['name'].strip()
            description = request.form['description'].strip()
            price = float(request.form['price'])
            quantity = int(request.form['quantity'])
            category = request.form['category'].strip()
            
            sweet = Sweet(name, description, price, quantity, category)
            shop.add_sweet(sweet)
            
            return redirect(url_for('view_sweets'))
        except ValueError as e:
            error = str(e)
        except Exception as e:
            error = f"Error adding sweet: {e}"
    else:
        error = None
    
    template = BASE_TEMPLATE.replace('{% block content %}{% endblock %}', """
        <div class="card">
            <h2>Add New Sweet</h2>
            
            {% if error %}
            <div class="alert alert-error">{{ error }}</div>
            {% endif %}
            
            <form method="POST">
                <div class="form-group">
                    <label for="name">Sweet Name:</label>
                    <input type="text" id="name" name="name" required>
                </div>
                
                <div class="form-group">
                    <label for="description">Description:</label>
                    <textarea id="description" name="description" rows="3" required></textarea>
                </div>
                
                <div class="form-group">
                    <label for="price">Price (INR):</label>
                    <input type="number" id="price" name="price" step="0.01" min="0" required>
                </div>
                
                <div class="form-group">
                    <label for="quantity">Quantity:</label>
                    <input type="number" id="quantity" name="quantity" min="0" required>
                </div>
                
                <div class="form-group">
                    <label for="category">Category:</label>
                    <input type="text" id="category" name="category" required>
                </div>
                
                <button type="submit">Add Sweet</button>
                <a href="/sweets" style="margin-left: 1rem; color: #666; text-decoration: none;">Cancel</a>
            </form>
        </div>
    """)
    
    return render_template_string(template,
                                title="Add Sweet",
                                shop_name=shop.name,
                                error=error)

@app.route('/search')
def search():
    query = request.args.get('q', '')
    results = []
    
    if query:
        results = shop.search_sweets(query)
    
    template = BASE_TEMPLATE.replace('{% block content %}{% endblock %}', """
        <div class="card">
            <h2>Search Sweets</h2>
            
            <form method="GET" class="search-bar">
                <input type="text" name="q" placeholder="Search by name, description, or category..." value="{{ query }}">
                <button type="submit">Search</button>
            </form>
            
            {% if query %}
                <h3>Search Results for "{{ query }}" ({{ results|length }} found)</h3>
                
                {% if results %}
                <div class="sweet-grid">
                    {% for sweet in results %}
                    <div class="sweet-card">
                        <div class="sweet-id">{{ sweet.id }}</div>
                        <div class="sweet-name">{{ sweet.name }}</div>
                        <div class="sweet-price">₹{{ "%.2f"|format(sweet.price) }}</div>
                        <div class="sweet-category">{{ sweet.category }}</div>
                        <p>{{ sweet.description }}</p>
                        <p><strong>Stock:</strong> {{ sweet.quantity }} available</p>
                    </div>
                    {% endfor %}
                </div>
                {% else %}
                <p>No sweets found matching your search.</p>
                {% endif %}
            {% endif %}
        </div>
    """)
    
    return render_template_string(template,
                                title="Search",
                                shop_name=shop.name,
                                query=query,
                                results=results)

@app.route('/categories')
def categories():
    categories = shop.get_categories()
    category_data = []
    
    for category in sorted(categories):
        sweets = shop.get_sweets_by_category(category)
        category_data.append({
            'name': category,
            'count': len(sweets),
            'sweets': sweets
        })
    
    template = BASE_TEMPLATE.replace('{% block content %}{% endblock %}', """
        <div class="card">
            <h2>Sweet Categories</h2>
            
            {% for cat in category_data %}
            <div class="card">
                <h3>{{ cat.name }} ({{ cat.count }} sweets)</h3>
                <div class="sweet-grid">
                    {% for sweet in cat.sweets %}
                    <div class="sweet-card">
                     <div class="sweet-id">{{ sweet.id }}</div>
                        <div class="sweet-name">{{ sweet.name }}</div>
                        <div class="sweet-price">₹{{ "%.2f"|format(sweet.price) }}</div>
                        <p>{{ sweet.description }}</p>
                        <p><strong>Stock:</strong> {{ sweet.quantity }} available</p>
                    </div>
                    {% endfor %}
                </div>
            </div>
            {% endfor %}
        </div>
    """)
    
    return render_template_string(template,
                                title="Categories",
                                shop_name=shop.name,
                                category_data=category_data)

@app.route('/statistics')
def statistics():
    stats = {
        'total_sweets': len(shop),
        'available_sweets': len(shop.get_available_sweets()),
        'out_of_stock': len(shop) - len(shop.get_available_sweets()),
        'total_value': shop.get_total_value(),
        'categories': shop.get_categories(),
        'low_stock': shop.get_low_stock_sweets(10)
    }
    
    template = BASE_TEMPLATE.replace('{% block content %}{% endblock %}', """
        <div class="card">
            <h2>Shop Statistics</h2>
            
            <div class="stats">
                <div class="stat-card">
                    <div class="stat-number">{{ stats.total_sweets }}</div>
                    <div class="stat-label">Total Sweet Types</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">{{ stats.available_sweets }}</div>
                    <div class="stat-label">Available Types</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">{{ stats.out_of_stock }}</div>
                    <div class="stat-label">Out of Stock</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">₹{{ "%.2f"|format(stats.total_value) }}</div>
                    <div class="stat-label">Total Inventory Value</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">{{ stats.categories|length }}</div>
                    <div class="stat-label">Categories</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">{{ stats.low_stock|length }}</div>
                    <div class="stat-label">Low Stock Items</div>
                </div>
            </div>
            
            <div class="card">
                <h3>Categories</h3>
                <p>{{ stats.categories|join(', ') }}</p>
            </div>
            
            {% if stats.low_stock %}
            <div class="card">
                <h3>Low Stock Alert (≤ 10 items)</h3>
                <table>
                    <thead>
                        <tr>
                            <th>id</th>
                            <th>Name</th>
                            <th>Quantity</th>
                            <th>Category</th>
                            <th>Price</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for sweet in stats.low_stock %}
                        <tr>
                            <td>{{sweet.id}}</td>
                            <td>{{ sweet.name }}</td>
                            <td style="color: #e74c3c; font-weight: bold;">{{ sweet.quantity }}</td>
                            <td>{{ sweet.category }}</td>
                            <td>₹{{ "%.2f"|format(sweet.price) }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
            {% endif %}
        </div>
    """)
    
    return render_template_string(template,
                                title="Statistics",
                                shop_name=shop.name,
                                stats=stats)

@app.route('/edit/<name>', methods=['GET', 'POST'])
def edit_sweet(name):
    sweet = shop.get_sweet(name)
    if not sweet:
        return redirect(url_for('view_sweets'))
    
    error = None
    if request.method == 'POST':
        try:
            updates = {}
            
            new_desc = request.form['description'].strip()
            if new_desc != sweet.description:
                updates['description'] = new_desc
            
            new_price = float(request.form['price'])
            if new_price != sweet.price:
                updates['price'] = new_price
            
            new_qty = int(request.form['quantity'])
            if new_qty != sweet.quantity:
                updates['quantity'] = new_qty
            
            new_cat = request.form['category'].strip()
            if new_cat != sweet.category:
                updates['category'] = new_cat
            
            if updates:
                shop.update_sweet(name, **updates)
            
            return redirect(url_for('view_sweets'))
        except ValueError as e:
            error = str(e)
        except Exception as e:
            error = f"Error updating sweet: {e}"
    
    template = BASE_TEMPLATE.replace('{% block content %}{% endblock %}', """
        <div class="card">
            <h2>Edit Sweet: {{ sweet.name }}</h2>
            
            {% if error %}
            <div class="alert alert-error">{{ error }}</div>
            {% endif %}
            
            <form method="POST">
                <div class="form-group">
                    <label for="description">Description:</label>
                    <textarea id="description" name="description" rows="3" required>{{ sweet.description }}</textarea>
                </div>
                
                <div class="form-group">
                    <label for="price">Price (INR):</label>
                    <input type="number" id="price" name="price" step="0.01" min="0" value="{{ sweet.price }}" required>
                </div>
                
                <div class="form-group">
                    <label for="quantity">Quantity:</label>
                    <input type="number" id="quantity" name="quantity" min="0" value="{{ sweet.quantity }}" required>
                </div>
                
                <div class="form-group">
                    <label for="category">Category:</label>
                    <input type="text" id="category" name="category" value="{{ sweet.category }}" required>
                </div>
                
                <button type="submit">Update Sweet</button>
                <a href="/sweets" style="margin-left: 1rem; color: #666; text-decoration: none;">Cancel</a>
            </form>
        </div>
    """)
    
    return render_template_string(template,
                                title=f"Edit {sweet.name}",
                                shop_name=shop.name,
                                sweet=sweet,
                                error=error)

@app.route('/delete/<name>')
def delete_sweet(name):
    try:
        shop.remove_sweet(name)
    except ValueError:
        pass  # Sweet not found, ignore
    
    return redirect(url_for('view_sweets'))

if __name__ == '__main__':
    print("Starting Sweet Shop Web Application...")
    print("Visit http://localhost:5000 to access the web interface")
    app.run(debug=True, host='0.0.0.0', port=5000)

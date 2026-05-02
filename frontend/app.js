document.addEventListener('DOMContentLoaded', () => {
    const API_URL = '/api/recipe/recipes/';
    const recipeGrid = document.getElementById('recipeGrid');
    const searchInput = document.getElementById('searchInput');

    // Fetch recipes from the API
    async function fetchRecipes(query = '') {
        try {
            const url = query ? `${API_URL}?search=${encodeURIComponent(query)}` : API_URL;
            const response = await fetch(url);
            
            if (!response.ok) {
                throw new Error('Failed to fetch recipes');
            }
            
            const data = await response.json();
            // Since we added pagination, the recipes are in data.results
            const recipes = data.results || data; 
            
            renderRecipes(recipes);
        } catch (error) {
            console.error('Error fetching recipes:', error);
            recipeGrid.innerHTML = `
                <div class="loading-state" style="color: var(--zomato-red);">
                    Oops! Unable to load recipes. Please make sure the Django server is running.
                </div>
            `;
        }
    }

    // Render recipes to the DOM
    function renderRecipes(recipes) {
        recipeGrid.innerHTML = ''; // Clear loading state

        if (recipes.length === 0) {
            recipeGrid.innerHTML = `
                <div class="loading-state">
                    No delicious recipes found right now.
                </div>
            `;
            return;
        }

        recipes.forEach(recipe => {
            // Generate tags HTML
            const tagsHTML = recipe.tags && recipe.tags.length > 0 
                ? recipe.tags.map(tag => `<span class="tag">${tag.name}</span>`).join('')
                : '<span class="tag">Standard</span>';

            // Use provided image or fallback placeholder
            const imageSrc = recipe.image || 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80';

            const card = document.createElement('div');
            card.className = 'recipe-card';
            card.innerHTML = `
                <img src="${imageSrc}" alt="${recipe.title}" class="recipe-image">
                <div class="recipe-info">
                    <div class="recipe-header">
                        <h3 class="recipe-title">${recipe.title}</h3>
                        <span class="recipe-price">₹${recipe.price}</span>
                    </div>
                    <div class="recipe-meta">
                        <div class="meta-item">
                            <span>⏱️</span> ${recipe.time_minutes} mins
                        </div>
                        <div class="meta-item">
                            <span>⭐</span> 4.5
                        </div>
                    </div>
                    <div class="tags-container">
                        ${tagsHTML}
                    </div>
                </div>
            `;
            recipeGrid.appendChild(card);
        });
    }

    // Initialize fetching
    fetchRecipes();

    // Search functionality with basic debounce
    let timeoutId;
    searchInput.addEventListener('input', (e) => {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => {
            fetchRecipes(e.target.value);
        }, 500);
    });
});

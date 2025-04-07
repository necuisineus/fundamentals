import ipywidgets as widgets
from IPython.display import display, clear_output
import json
from datetime import datetime
from google.colab import files  # For file download in Colab
import uuid
import hashlib
import unicodedata
import string
import re

def generate_uuid():
    return str(uuid.uuid4())

def generate_concept_hash(recipe):
    # Only include the persistent part: the recipe concept.
    concept = recipe.get("recipeConcept", "")
    # Normalize Unicode (NFKC), lowercase, collapse whitespace, and remove punctuation.
    normalized = unicodedata.normalize('NFKC', concept)
    normalized = " ".join(normalized.lower().split())
    normalized = normalized.translate(str.maketrans('', '', string.punctuation))
    return hashlib.md5(normalized.encode("utf-8")).hexdigest()

def generate_filename(recipe):
    # Use recipe name, yield, and recipe concept to build the filename.
    name = recipe.get("name", "recipe")
    yield_val = recipe.get("recipeYield", "unknown")
    concept = recipe.get("recipeConcept", "concept")
    filename = f"{name}_{yield_val}_{concept}"
    # Normalize: lowercase, replace spaces with underscores, remove non-alphanumeric characters.
    filename = filename.lower()
    filename = re.sub(r'\s+', '_', filename)
    filename = re.sub(r'[^a-z0-9_]', '', filename)
    return filename + ".json"

# Generate today's date in ISO format (YYYY-MM-DD)
today_date = datetime.today().strftime("%Y-%m-%d")

# Define styles and layouts
custom_style = {'description_width': '200px'}
input_layout = widgets.Layout(width='800px')       # For single-line widgets
textarea_layout = widgets.Layout(width='800px', height='200px')  # For multi-line widgets
container_layout = widgets.Layout(margin='0 0 0 50px', width='1000px')
output = widgets.Output(layout=widgets.Layout(width='1000px'))

# Basic Recipe Info
recipe_name = widgets.Text(
    description='Recipe Name:',
    placeholder='Enter recipe name',
    style=custom_style,
    layout=input_layout
)
date_created = widgets.Text(
    description='Date Created:',
    placeholder='YYYY-MM-DD Format',
    style=custom_style,
    layout=input_layout
)
deploy_date = widgets.Text(
    description='Deploy Dates:',
    placeholder='Comma separated YYYY-MM-DD Format (e.g., 2023-10-08, 2024-10-12)',
    style=custom_style,
    layout=input_layout
)

# Author Information
author_name = widgets.Text(
    description='Author Name:',
    value='Northeast Cuisine',
    style=custom_style,
    layout=input_layout
)
author_url = widgets.Text(
    description='Author URL:',
    value='northeastcuisineus.substack.com',
    style=custom_style,
    layout=input_layout
)

# Verification Information
verification_name = widgets.Text(
    description='Verification Name:',
    value='Northeast Cuisine',
    style=custom_style,
    layout=input_layout
)
verification_status = widgets.Dropdown(
    description='Verification:',
    options=['verified', 'unverified', 'approximated'],
    style=custom_style,
    layout=input_layout
)
verification_method = widgets.Dropdown(
    description='Method:',
    options=['workshop', 'coursed dinner', 'restaurant', 'institution', 'unverified', 'approximated'],
    style=custom_style,
    layout=input_layout
)
verification_date = widgets.Text(
    description='Verif. Date:',
    placeholder=today_date,
    style=custom_style,
    layout=input_layout
)

# Score Information
score_eq = widgets.IntText(
    description='Score Eq:',
    placeholder=100,
    style=custom_style,
    layout=input_layout
)
score_vm = widgets.IntText(
    description='Score Vm:',
    placeholder=100,
    style=custom_style,
    layout=input_layout
)
score_total = widgets.IntText(
    description='Score Total:',
    placeholder=100,
    style=custom_style,
    layout=input_layout
)
score_alap = widgets.IntText(
    description='Score ALAP:',
    placeholder=100,
    style=custom_style,
    layout=input_layout
)

# Additional Recipe Details
recipe_concept = widgets.Text(
    description='Recipe Concept:',
    placeholder='Enter recipe concept',
    style=custom_style,
    layout=input_layout
)
alternative_names = widgets.Text(
    description='Alt. Names:',
    placeholder='Comma separated (e.g., Cabbage Roll, Golumpki)',
    style=custom_style,
    layout=input_layout
)
recipe_cuisine = widgets.Text(
    description='Cuisine:',
    value='Northeast United States',
    style=custom_style,
    layout=input_layout
)
recipe_category = widgets.Text(
    description='Category:',
    placeholder='emulsion',
    style=custom_style,
    layout=input_layout
)
prep_time = widgets.Text(
    description='Prep Time:',
    placeholder='PT10M',
    style=custom_style,
    layout=input_layout
)
cook_time = widgets.Text(
    description='Cook Time:',
    placeholder='PT10M',
    style=custom_style,
    layout=input_layout
)
total_time = widgets.Text(
    description='Total Time:',
    placeholder='PT20M',
    style=custom_style,
    layout=input_layout
)
recipe_yield = widgets.Text(
    description='Yield:',
    placeholder='6',
    style=custom_style,
    layout=input_layout
)

# Dynamic Ingredient Entry Section
ingredient_rows = []  # To store (quantity, measurement, ingredient) widget tuples
ingredient_container = widgets.VBox(layout=input_layout)
add_ingredient_button = widgets.Button(
    description="Add Ingredient",
    layout=widgets.Layout(width='200px')
)

def add_ingredient_row(b):
    quantity_widget = widgets.Text(placeholder="Quantity", layout=widgets.Layout(width="200px"))
    measurement_widget = widgets.Text(placeholder="Measurement", layout=widgets.Layout(width="200px"))
    ingredient_widget = widgets.Text(placeholder="Ingredient", layout=widgets.Layout(width="400px"))
    row = widgets.HBox([quantity_widget, measurement_widget, ingredient_widget])
    ingredient_rows.append((quantity_widget, measurement_widget, ingredient_widget))
    ingredient_container.children += (row,)

add_ingredient_button.on_click(add_ingredient_row)
# Add a default ingredient row.
add_ingredient_row(None)

# Dynamic Instruction Entry Section
instruction_rows = []  # To store (step name, step text) widget tuples
instruction_container = widgets.VBox(layout=input_layout)
add_instruction_button = widgets.Button(
    description="Add Instruction",
    layout=widgets.Layout(width='200px')
)

def add_instruction_row(b):
    step_name_widget = widgets.Text(placeholder="Step Name", layout=widgets.Layout(width="200px"))
    step_text_widget = widgets.Text(placeholder="Step Text", layout=widgets.Layout(width="600px"))
    row = widgets.HBox([step_name_widget, step_text_widget])
    instruction_rows.append((step_name_widget, step_text_widget))
    instruction_container.children += (row,)

add_instruction_button.on_click(add_instruction_row)
# Add a default instruction row.
add_instruction_row(None)

# Nutrition and Other Fields
nutrition = widgets.Textarea(
    description='Nutrition:',
    placeholder='One per line: key: value',
    style=custom_style,
    layout=input_layout
)
description_widget = widgets.Textarea(
    description='Description:',
    placeholder='Enter description',
    style=custom_style,
    layout=input_layout
)
suitable_for_diet = widgets.Text(
    description='Suitable Diet:',
    placeholder='Comma separated URLs (e.g., https://schema.org/LowFatDiet)',
    style=custom_style,
    layout=input_layout
)
estimated_cost = widgets.Text(
    description='Est. Cost:',
    placeholder='10.25',
    style=custom_style,
    layout=input_layout
)
tools = widgets.Text(
    description='Tools:',
    placeholder='Comma separated (e.g., 8in Stock Pot)',
    style=custom_style,
    layout=input_layout
)
citation = widgets.Text(
    description='Citation:',
    placeholder='Gordon_Ramsey',
    style=custom_style,
    layout=input_layout
)
comment = widgets.Textarea(
    description='Comment:',
    placeholder='Enter any comment',
    style=custom_style,
    layout=input_layout
)
keywords = widgets.Text(
    description='Keywords:',
    placeholder='Comma separated (e.g., cheese, pork, keto)',
    style=custom_style,
    layout=input_layout
)
maintainer = widgets.Text(
    description='Maintainer:',
    value='Northeast_Cuisine',
    style=custom_style,
    layout=input_layout
)
content_location = widgets.Text(
    description='Content Loc:',
    value='PA_Philadelphia',
    style=custom_style,
    layout=input_layout
)
spatial_coverage = widgets.Text(
    description='Spatial Cov:',
    value='US_Northeast',
    style=custom_style,
    layout=input_layout
)

# Filename Widget for custom naming (if desired)
filename_widget = widgets.Text(
    description='Filename:',
    value='',  # Leave empty to auto-generate based on naming convention.
    placeholder='Leave blank for auto-generated name. [Format is Recipe Concept_Serving Size_Recipe Name]',
    style=custom_style,
    layout=input_layout
)

# Button to generate the JSON
generate_button = widgets.Button(
    description='Generate JSON',
    style=custom_style,
    layout=input_layout
)

def on_generate_button_clicked(b):
    with output:
        clear_output()
        # Build the JSON object using the widget values.
        recipe = {
            "@context": "https://schema.org/",
            "@type": "Recipe",
            "uuid": generate_uuid(),
            "name": recipe_name.value,
            "date": {
                "dateCreated": date_created.value,
                "deployDate": [d.strip() for d in deploy_date.value.split(",") if d.strip()]
            },
            "author": {
                "@type": "Organization",
                "name": author_name.value,
                "url": author_url.value
            },
            "verification": {
                "name": verification_name.value,
                "verification": verification_status.value,
                "method": verification_method.value,
                "verificationDate": verification_date.value
            },
            "score": {
                "Eq": score_eq.value,
                "Vm": score_vm.value,
                "Total": score_total.value,
                "ALAP": score_alap.value
            },
            "recipeConcept": recipe_concept.value,
            "nameEquals": [n.strip() for n in alternative_names.value.split(",") if n.strip()],
            "recipeCuisine": recipe_cuisine.value,
            "recipeCategory": recipe_category.value,
            "prepTime": prep_time.value,
            "cookTime": cook_time.value,
            "totalTime": total_time.value,
            "recipeYield": recipe_yield.value,
            "recipeIngredient": [],
            "recipeInstructions": [],
            "nutrition": {},
            "description": description_widget.value,
            "suitableForDiet": [d.strip() for d in suitable_for_diet.value.split(",") if d.strip()],
            "estimatedCost": estimated_cost.value,
            "tool": [t.strip() for t in tools.value.split(",") if t.strip()],
            "citation": citation.value,
            "comment": comment.value,
            "keywords": [k.strip() for k in keywords.value.split(",") if k.strip()],
            "maintainer": maintainer.value,
            "contentLocation": content_location.value,
            "spatialCoverage": spatial_coverage.value
        }
        # Process ingredient rows.
        for quantity_widget, measurement_widget, ingredient_widget in ingredient_rows:
            quantity = quantity_widget.value.strip()
            measurement = measurement_widget.value.strip()
            ingredient_text = ingredient_widget.value.strip()
            if ingredient_text:  # Only include if ingredient field is provided.
                ingredient_obj = {
                    "quantity": quantity,
                    "measurement": measurement,
                    "ingredient": ingredient_text
                }
                recipe["recipeIngredient"].append(ingredient_obj)

        # Process instruction rows.
        for step_name_widget, step_text_widget in instruction_rows:
            step_name = step_name_widget.value.strip()
            step_text = step_text_widget.value.strip()
            if step_name or step_text:  # Include if either field has content.
                recipe["recipeInstructions"].append({
                    "@type": "HowToStep",
                    "name": step_name,
                    "text": step_text
                })

        # Process nutrition (each line should be "key: value").
        for line in nutrition.value.splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                recipe["nutrition"][key.strip()] = value.strip()

        # Add the deterministic hash based on recipeConcept.
        recipe["conceptHash"] = generate_concept_hash(recipe)

        # Convert the recipe to JSON.
        json_output = json.dumps(recipe, indent=4)
        print("Generated Recipe JSON:")
        print(json_output)

        # Determine the filename.
        custom_filename = filename_widget.value.strip()
        if custom_filename:
            filename = custom_filename if custom_filename.lower().endswith('.json') else custom_filename + '.json'
        else:
            filename = generate_filename(recipe)

        # Write the JSON to a file and trigger a download (Google Colab only).
        with open(filename, "w") as f:
            f.write(json_output)
        files.download(filename)

generate_button.on_click(on_generate_button_clicked)

# Assemble all widgets into a list.
widgets_list = [
    recipe_name, date_created, deploy_date,
    author_name, author_url,
    verification_name, verification_status, verification_method, verification_date,
    score_eq, score_vm, score_total, score_alap,
    recipe_concept, alternative_names, recipe_cuisine, recipe_category,
    prep_time, cook_time, total_time, recipe_yield,
    # For ingredients, display the add button and dynamic container.
    widgets.VBox([add_ingredient_button, ingredient_container]),
    # For instructions, display the add button and dynamic container.
    widgets.VBox([add_instruction_button, instruction_container]),
    nutrition,
    description_widget, suitable_for_diet, estimated_cost, tools,
    citation, comment, keywords, maintainer, content_location, spatial_coverage,
    filename_widget,  # New filename widget.
    generate_button, output
]

# Wrap all widgets in a VBox with the specified container layout.
container = widgets.VBox(widgets_list, layout=container_layout)
# Use this cell to display the container and make the JSON File
display(container)
# Recipe Template Documentation

## Overview

This document describes the structure of the JSON recipe template, following the [schema.org](https://schema.org/) standard. It provides details on each key, its expected values, and its significance.

## JSON Structure

### General Metadata

- `@context`: *(String)* The URL for the schema.org context.

  - Example: `"https://schema.org/"`

- `@type`: *(String)* Specifies the type of schema. Always "Recipe".

  - Example: `"Recipe"`

- `name`: *(String)* The name of the recipe, ideally containing key ingredients for easier searchability.

  - Example: `"Fall Chili with mangalitsa pork, eggplant, peppers, and dragon tongue beans"`

### Date Information

- `date`: *(Object)* Holds different date-related details.
  - `dateCreated`: *(String)* The date when the recipe was authored.
    - Example: `"October 5, 2022"`
  - `deployDate`: *(Array of Strings)* List of dates when the recipe was used or deployed. In the future, this field updates automatically from a application designed to help chefs in all contexts deploy recipes.
    - Example: `["October 5, 2022, "October 8, 2023", "October 12, 2024"]`

### Author Information

- `author`: *(Object)* Details about the recipe's author.
  - `@type`: *(String)* Either "Person" or "Organization".
  - `name`: *(String)* Name of the author or organization.
  - `url`: *(String)* Website or link to the author's work.
  - Example:
    ```json
    {
        "@type": "Organization",
        "name": "Northeast Cuisine",
        "url": "northeastcuisineus.substack.com"
    }
    ```

### Verification

- `verification`: *(Object)* Verification details.
  - `name`: *(String)* Name of the verifying entity.
  - `verification`: *(String)* Status: "verified" (VRI), "unverified" (URI), or "approximated". More on this in the article [Recipe Concepts, Recipes & Dynamic Recipes.](https://northeastcuisineus.substack.com/p/recipe-concepts-recipes-and-dynamic)
  - `method`: *(String)* Method of verification. Dinner, workshop, restarant, cafeteria, etc.
  - `verificationDate`: *(String)* Date when verification was first recorded.
  - Example:
    ```json
    {
        "name": "Northeast Cuisine",
        "verification": "verified",
        "method": "test",
        "verificationDate": "October 8, 2022"
    }
    ```

### Recipe Categorization

- `recipeConcept`: *(String)* Recipe concept as detailed in [Recipe Concepts, Recipes & Dynamic Recipes.](https://northeastcuisineus.substack.com/p/recipe-concepts-recipes-and-dynamic) All recipes are tied to a recipe concept.

  - Example: `"Chili"`

- `nameEquals`: *(Array of Strings)* Alternative names for the dish in different cultures around the world and inside the U.S. While the recipe concept itself is relative to the geo-cultural area that it is from or related to, the concepts are kin to one another albeit their own unique kind. Understanding similar naming conventions gives culture context and richer information on the dishes and their relation to cultural diaspora.

  - Example: `["Cabbage Roll", "Golumpki"]`

- `recipeCuisine`: *(String)* The cuisine classification. This data represents what type of cuisine the recipe is, for us it will always be 'Northeast United States'. Cuisine is emergent, it can be influenced but mostly must be practiced within an area and crucially, the home.

  - Example: `"Northeast United States"`

- `recipeCategory`: *(String)* A functional classification of the dish. This is where interpretation starts to really fall into play. This field in the schema.org conception, is supposed to identify the course time or perception of the dish itself such as appetizer or entree. However, viewing categories in this way is vague and highly interpretable. A meatball sub is a meal, a meatball on a stick is an appetizer. We will use this designation to identify more general category naming conventions. For example, how sauces in modern perception are a reduction, emulsion, or a puree. These descriptions are a lot more indicative of what category something is functionally rather then when and how it is perceived in the dining order.

  - Example: `"Emulsion"`

### Preparation and Cooking Times

- `prepTime`: *(String)* Preparation time in ISO 8601 format.

  - Example: `"PT10M"` (10 minutes)

- `cookTime`: *(String)* Cooking time in ISO 8601 format.

  - Example: `"PT10M"` (10 minutes)

- `totalTime`: *(String)* Total time required in ISO 8601 format. (prepTime + cookTime).

  - Example: `"PT20M"`

### Yield and Ingredients

- `recipeYield`: *(Integer/String)* Number of servings. This is a very critical piece of information to have as an integer and not as a range or string ("word"). The recipe yield becomes part of an integrated costing equation in regards to SL food.

  - Example: `"6"`

- `recipeIngredient`: *(Array of Objects)* List of dictionaries of ingredients for this recipe, separated by comma. This will be separated into quantity, measurement, and ingredient. The ingredients can be expanded into complex data with even more attributes.

  - Example:
    ```json
    [
        {"quantity": "3", "measurement": "tablespoons", "ingredient": "buttermilk"}
    ]
    ```

### Instructions

- `recipeInstructions`: *(Array of Strings)* Step-by-step directions.
  - Example: `["Step 1", "Step 2"]`

### Nutrition

- `nutrition`: *(Object)* Nutritional information.
  - Example: `{"Calories: "888"}`

### Additional Metadata

- `description`: *(String)* A description of the recipe.

  - Example: `"description of the recipe"`

- `suitableForDiet`: *(Array of Strings)* Dietary considerations, using schema.org standards.

  - Example: `["https://schema.org/LowFatDiet", "https://schema.org/GlutenFreeDiet"]`

- `estimatedCost`: *(String)* Estimated total cost in USD.

  - Example: `"10.25"`

### Tools and Citations

- `tool`: *(Array of Strings)* Tools used to make the recipe. This is an important component of deployment and designing menus and restaurant architecture.

  - Example: `["8in Stock Pot"]`

- `citation`: *(String)* A citation or reference to another creative work, such as another publication, web page, scholarly article, etc. In this context, when we refer to other recipes or chefs or inspiration for this recipe. This is not necessarily a citation like in academia, but more of a nod to a lineage of cultural or professional understanding and influence.

  - Example: `"Gordon_Ramsey"`

- `comment`: *(String)* User comments. Perhaps as a social commentary piece of diners and those who eat.

  - Example: `""`

### Keywords and Metadata Management

- `keywords`: *(Array of Strings)* Tags for searchability.

  - Example: `["nameEquals", "pork", "keto"]`

- `maintainer`: *(String)* A maintainer of a Dataset, software package (SoftwareApplication), or other Project. A maintainer is a Person or Organization that manages contributions to, and/or publication of, some (typically complex) artifact. It is common for distributions of software and data to be based on "upstream" sources. When maintainer is applied to a specific version of something e.g. a particular version or packaging of a Dataset, it is always possible that the upstream source has a different maintainer. The isBasedOn property can be used to indicate such relationships between datasets to make the different maintenance roles clear. Similarly in the case of software, a package may have dedicated maintainers working on integration into software distributions such as Ubuntu, as well as upstream maintainers of the underlying work.

  - Example: `"Northeast_Cuisine"`

### Location Information

- `contentLocation`: *(String)* Geographic context for the recipe. The location depicted or described in the content. Not necessarily related to what we are describing in the content, but the geographic context in which a recipe is being prepared is related to the rest of the important data.

  - Example: `"PA_Philadelphia"`

- `spatialCoverage`: *(String)* General region covered. Defining the area of Northeast

  - Example: `"US_Northeast"`

---

This documentation provides a structured overview of the JSON schema used for recipe representation. It ensures consistency and clarity in defining, categorizing, and verifying recipes.


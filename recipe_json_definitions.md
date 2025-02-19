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
  - `deployDate`: *(Array of Strings)* List of dates when the recipe was used or deployed.
    - Example: `["October 8, 2023", "October 12, 2024"]`

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
  - `verification`: *(String)* Status: "verified" (VRI), "unverified" (URI), or "approximated".
  - `method`: *(String)* Method of verification.
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

- `recipeConcept`: *(String)* General concept of the recipe.

  - Example: `"Chili"`

- `nameEquals`: *(Array of Strings)* Alternative names for the dish in different cultures.

  - Example: `["Cabbage Roll", "Golumpki"]`

- `recipeCuisine`: *(String)* The cuisine classification.

  - Example: `"Northeast United States"`

- `recipeCategory`: *(String)* A functional classification of the dish.

  - Example: `"Emulsion"`

### Preparation and Cooking Times

- `prepTime`: *(String)* Preparation time in ISO 8601 format.

  - Example: `"PT10M"` (10 minutes)

- `cookTime`: *(String)* Cooking time in ISO 8601 format.

  - Example: `"PT10M"` (10 minutes)

- `totalTime`: *(String)* Total time required.

  - Example: `"PT20M"`

### Yield and Ingredients

- `recipeYield`: *(Integer/String)* Number of servings.

  - Example: `"6"`

- `recipeIngredient`: *(Array of Objects)* List of ingredients with quantity and measurement.

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

- `nutrition`: *(Object)* Nutritional information (to be filled using Wolfram Nutrition).
  - Example: `{}`

### Additional Metadata

- `description`: *(String)* A brief description of the recipe.

  - Example: `""`

- `suitableForDiet`: *(Array of Strings)* Dietary considerations, using schema.org standards.

  - Example: `["https://schema.org/LowFatDiet", "https://schema.org/GlutenFreeDiet"]`

- `estimatedCost`: *(String)* Estimated total cost in USD.

  - Example: `"10.25"`

### Tools and Citations

- `tool`: *(Array of Strings)* Required kitchen tools.

  - Example: `["8in Stock Pot"]`

- `citation`: *(String)* A reference to a source or inspiration.

  - Example: `"Gordon_Ramsey"`

- `comment`: *(String)* User comments.

  - Example: `""`

### Keywords and Metadata Management

- `keywords`: *(Array of Strings)* Tags for searchability.

  - Example: `["nameEquals", "pork", "keto"]`

- `maintainer`: *(String)* Name of the maintainer.

  - Example: `"Northeast_Cuisine"`

### Location Information

- `contentLocation`: *(String)* Geographic context for the recipe.

  - Example: `"PA_Philadelphia"`

- `spatialCoverage`: *(String)* General region covered.

  - Example: `"US_Northeast"`

---

This documentation provides a structured overview of the JSON schema used for recipe representation. It ensures consistency and clarity in defining, categorizing, and verifying recipes.


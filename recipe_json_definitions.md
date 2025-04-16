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

- **date:** (Object) Holds different date-related details.
  - **dateCreated:** (String) The date when the recipe was authored, in ISO 8601 format (YYYY-MM-DD).  
    **Example:** `"2022-10-05"`
  - **deployDate:** (Array of Strings) A list of dates when the recipe was used or deployed. In the future, this field will update automatically from an application designed to help chefs in all contexts deploy recipes, using the ISO 8601 date format.  
    **Example:** `["2022-10-05", "2023-10-08", "2024-10-12"]`

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
### Scoring Information

- `score`: *(Object)* Represents scoring metrics associated with the recipe, used to evaluate culinary quality, presentation, locality of ingredients, and overall performance. Each metric is scored numerically, typically from 0 to 100.

  - `Eq`: *(Integer)* **Equal Weight**—Eq takes every ingredient in the recipe and weighs their impact the same. If your recipe has 15 ingredients, your score will be based on how many of those ingredients are SL.
    - Example: `100`

  - `Vm`: *(Integer)* **Volume/Mass**—Vm is taking each ingredient and standardizing their volume or mass to milliliters or grams respectively. Because certain ingredients comprise a larger portion of a recipe, they should be weighed more heavily than an ingredient that takes up a smaller portion.
    - Example: `95`

  - `ALAP`: *(Integer)* **As Local As Possible**— A special scoring metric to discuss items that do not score in the typical NEC Seasonal-Local metric, but where the ingredients are as local as possible.
    - Example: `84.64`

  - `Total`: *(Integer)* A combined or overall aggregate score representing the recipe's performance across all metrics.
    - Example: `97.5`

**Example JSON:**
```json
"score": {
  "Eq": 100,
  "Vm": 95,
  "ALAP": 84.64,
  "Total": 97.5
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
 
# ISO 8601 Duration Format for Recipe Times

The prep time, cook time, and total time should be represented using the ISO 8601 duration format. This format expresses a period of time in a concise, standardized way.

## Format

The general format is:


Where:
- **P** – Indicates the start of the period.
- **nY** – Number of years.
- **nM** – Number of months (if before the `T`, it represents months; if after the `T`, it represents minutes).
- **nD** – Number of days.
- **T** – Separator that indicates the start of the time component.
- **nH** – Number of hours.
- **nM** – Number of minutes.
- **nS** – Number of seconds.

## Examples

- **PT10M** – 10 minutes  
- **PT1H** – 1 hour  
- **PT1H30M** – 1 hour and 30 minutes  
- **PT45M** – 45 minutes  
- **PT30S** – 30 seconds  
- **P1D** – 1 day  
- **P1DT2H** – 1 day and 2 hours  
- **P2DT3H4M** – 2 days, 3 hours, and 4 minutes

*Note:* For most recipe applications, you'll likely use the time component only (e.g., `PT10M` or `PT1H30M`), but the full format is available if you need to represent longer durations.


### Yield and Ingredients

- `recipeYieldServings`: *(Integer/String)* Number of servings. This is a very critical piece of information to have as an integer and not as a range or string ("word"). The recipe yield becomes part of an integrated costing equation in regards to SL food.

  - Example: `"6"`
 
- `recipeYield`: *(Object)* The volume or weight of the resulting 'dish'. Helpful with core simple ingredients such as making butter or mascarpone where you want to understand a true yield for use in other recipes.

  - Example: `{"quantity: "225", measurement: "g"}`

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


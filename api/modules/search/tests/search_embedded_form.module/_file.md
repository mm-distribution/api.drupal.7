# modules/search/tests/search_embedded_form.module

- **Source:** [local](../../../../../source/modules/search/tests/search_embedded_form.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/tests/search_embedded_form.module) · 71 lines
- **Module/theme:** search_node_tags

## File documentation

```text
@file
Test module implementing a form that can be embedded in search results.

Embedded form are important, for example, for ecommerce sites where each
search result may included an embedded form with buttons like "Add to cart"
for each individual product (node) listed in the search results.
```

## Functions (derived index)

- [search_embedded_form_menu()](search_embedded_form_menu.md) — Implements hook_menu().
- [search_embedded_form_form()](search_embedded_form_form.md) — Builds a form for embedding in search results for testing.
- [search_embedded_form_form_submit()](search_embedded_form_form_submit.md) — Submit handler for search_embedded_form_form().
- [search_embedded_form_preprocess_search_result()](search_embedded_form_preprocess_search_result.md) — Adds the test form to search results.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._

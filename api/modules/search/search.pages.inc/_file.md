# modules/search/search.pages.inc

- **Source:** [local](../../../../source/modules/search/search.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.pages.inc) · 160 lines
- **Module/theme:** search

## File documentation

```text
@file
User page callbacks for the search module.
```

## Functions (derived index)

- [search_view()](search_view.md) — Menu callback; presents the search form and/or search results.
- [template_preprocess_search_results()](template_preprocess_search_results.md) — Process variables for search-results.tpl.php.
- [template_preprocess_search_result()](template_preprocess_search_result.md) — Process variables for search-result.tpl.php.
- [search_form_validate()](search_form_validate.md) — As the search form collates keys from other modules hooked in via hook_form_alter, the validation takes place in _submit. search_form_validate() is used solely to set the 'processed_keys' form value for the basic search form.
- [search_form_submit()](search_form_submit.md) — Process a search form submission.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._

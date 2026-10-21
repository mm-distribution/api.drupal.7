# modules/search/search-results.tpl.php

- **Source:** [local](../../../../source/modules/search/search-results.tpl.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search-results.tpl.php) · 36 lines
- **Module/theme:** search

## File documentation

```text
@file
Default theme implementation for displaying search results.

This template collects each invocation of theme_search_result(). This and
the child template are dependent to one another sharing the markup for
definition lists.

Note that modules may implement their own search type and theme function
completely bypassing this template.

Available variables:
- $search_results: All results as it is rendered through
  search-result.tpl.php
- $module: The machine-readable name of the module (tab) being searched, such
  as "node" or "user".


@see template_preprocess_search_results()

@ingroup themeable
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._

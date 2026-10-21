# template_process_html()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 2760–2772 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L2760-L2772)

## Signature

```php
function template_process_html(&$variables)
```

## Documentation

```text
Process variables for html.tpl.php

Perform final addition and modification of variables before passing into
the template. To customize these variables, call drupal_render() on elements
in $variables['page'] during THEME_preprocess_page().

@see template_preprocess_html()
@see html.tpl.php
```

## Code

```php
function template_process_html(&$variables) {
  // Render page_top and page_bottom into top level variables.
  $variables['page_top'] = drupal_render($variables['page']['page_top']);
  $variables['page_bottom'] = drupal_render($variables['page']['page_bottom']);
  // Place the rendered HTML for the page body into a top level variable.
  $variables['page']              = $variables['page']['#children'];
  $variables['page_bottom'] .= drupal_get_js('footer');

  $variables['head']    = drupal_get_html_head();
  $variables['css']     = drupal_add_css();
  $variables['styles']  = drupal_get_css();
  $variables['scripts'] = drupal_get_js();
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

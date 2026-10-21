# hook_html_head_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 3919–3926 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L3919-L3926)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_html_head_alter(&$head_elements)
```

## Documentation

```text
Alter XHTML HEAD tags before they are rendered by drupal_get_html_head().

Elements available to be altered are only those added using
drupal_add_html_head_link() or drupal_add_html_head(). CSS and JS files
are handled using drupal_add_css() and drupal_add_js(), so the head links
for those files will not appear in the $head_elements array.

@param $head_elements
  An array of renderable elements. Generally the values of the #attributes
  array will be the most likely target for changes.
```

## Code

```php
function hook_html_head_alter(&$head_elements) {
  foreach ($head_elements as $key => $element) {
    if (isset($element['#attributes']['rel']) && $element['#attributes']['rel'] == 'canonical') {
      // I want a custom canonical URL.
      $head_elements[$key]['#attributes']['href'] = mymodule_canonical_url();
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_html_head_alter()".

_None found._

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._

# drupal_js_defaults()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 4446–4460 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L4446-L4460)

## Signature

```php
function drupal_js_defaults($data = NULL)
```

## Documentation

```text
Constructs an array of the defaults that are used for JavaScript items.

@param $data
  (optional) The default data parameter for the JavaScript item array.

@see drupal_get_js()
@see drupal_add_js()
```

## Code

```php
function drupal_js_defaults($data = NULL) {
  return array(
    'type' => 'file',
    'group' => JS_DEFAULT,
    'every_page' => FALSE,
    'weight' => 0,
    'requires_jquery' => TRUE,
    'scope' => 'header',
    'cache' => TRUE,
    'defer' => FALSE,
    'preprocess' => TRUE,
    'version' => NULL,
    'data' => $data,
  );
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

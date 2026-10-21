# form_process_autocomplete()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 4025–4042 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L4025-L4042)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_process_autocomplete($element)
```

## Documentation

```text
Process function to prepare autocomplete data.

@param $element
  A textfield or other element with a #autocomplete_path.

@return array
  The processed form element.
```

## Code

```php
function form_process_autocomplete($element) {
  $element['#autocomplete_input'] = array();
  if ($element['#autocomplete_path'] && drupal_valid_path($element['#autocomplete_path'])) {
    $element['#autocomplete_input']['#id'] = $element['#id'] .'-autocomplete';
    // Force autocomplete to use non-clean URLs since this protects against the
    // browser interpreting the path plus search string as an actual file.
    $current_clean_url = isset($GLOBALS['conf']['clean_url']) ? $GLOBALS['conf']['clean_url'] : NULL;
    $GLOBALS['conf']['clean_url'] = 0;
    // Force the script path to 'index.php', in case the server is not
    // configured to find it automatically. Normally it is the responsibility
    // of the site to do this themselves using hook_url_outbound_alter() (see
    // url()) but since this code is forcing non-clean URLs on sites that don't
    // normally use them, it is done here instead.
    $element['#autocomplete_input']['#url_value'] = url($element['#autocomplete_path'], array('absolute' => TRUE, 'script' => 'index.php'));
    $GLOBALS['conf']['clean_url'] = $current_clean_url;
  }
  return $element;
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

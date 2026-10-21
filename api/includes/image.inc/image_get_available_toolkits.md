# image_get_available_toolkits()

- **Type:** Function
- **File:** [`includes/image.inc`](_file.md), lines 42–55 · [local source](../../../source/includes/image.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/image.inc#L42-L55)
- **Topics:** [image](../../topics/image.md)

## Signature

```php
function image_get_available_toolkits()
```

## Documentation

```text
Gets a list of available toolkits.

@return
  An array with the toolkit names as keys and the descriptions as values.
```

## Code

```php
function image_get_available_toolkits() {
  // hook_image_toolkits returns an array of toolkit names.
  $toolkits = module_invoke_all('image_toolkits');

  $output = array();
  foreach ($toolkits as $name => $info) {
    // Only allow modules that aren't marked as unavailable.
    if ($info['available']) {
      $output[$name] = $info['title'];
    }
  }

  return $output;
}
```

---
_Drupal 7.103 · [includes/image.inc](https://github.com/drupal/drupal/blob/7.103/includes/image.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

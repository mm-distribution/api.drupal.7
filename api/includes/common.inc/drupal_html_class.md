# drupal_html_class()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 4040–4049 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L4040-L4049)

## Signature

```php
function drupal_html_class($class)
```

## Documentation

```text
Prepares a string for use as a valid class name.

Do not pass one string containing multiple classes as they will be
incorrectly concatenated with dashes, i.e. "one two" will become "one-two".

@param $class
  The class name to clean.

@return
  The cleaned class name.
```

## Code

```php
function drupal_html_class($class) {
  // The output of this function will never change, so this uses a normal
  // static instead of drupal_static().
  static $classes = array();

  if (!isset($classes[$class])) {
    $classes[$class] = drupal_clean_css_identifier(drupal_strtolower($class));
  }
  return $classes[$class];
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

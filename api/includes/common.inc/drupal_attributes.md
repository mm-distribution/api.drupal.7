# drupal_attributes()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 2514–2520 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L2514-L2520)
- **Topics:** [sanitization](../../topics/sanitization.md)

## Signature

```php
function drupal_attributes(array $attributes = array())
```

## Documentation

```text
Converts an associative array to an XML/HTML tag attribute string.

Each array key and its value will be formatted into an attribute string.
If a value is itself an array, then its elements are concatenated to a single
space-delimited string (for example, a class attribute with multiple values).

Attribute values are sanitized by running them through check_plain().
Attribute names are not automatically sanitized. When using user-supplied
attribute names, it is strongly recommended to allow only white-listed names,
since certain attributes carry security risks and can be abused.

Examples of security aspects when using drupal_attributes:
@code
  // By running the value in the following statement through check_plain,
  // the malicious script is neutralized.
  drupal_attributes(array('title' => t('<script>steal_cookie();</script>')));

  // The statement below demonstrates dangerous use of drupal_attributes, and
  // will return an onmouseout attribute with JavaScript code that, when used
  // as attribute in a tag, will cause users to be redirected to another site.
  //
  // In this case, the 'onmouseout' attribute should not be whitelisted --
  // you don't want users to have the ability to add this attribute or others
  // that take JavaScript commands.
  drupal_attributes(array('onmouseout' => 'window.location="http://malicious.com/";')));
@endcode

@param $attributes
  An associative array of key-value pairs to be converted to attributes.

@return
  A string ready for insertion in a tag (starts with a space).

@ingroup sanitization
```

## Code

```php
function drupal_attributes(array $attributes = array()) {
  foreach ($attributes as $attribute => &$data) {
    $data = implode(' ', (array) $data);
    $data = $attribute . '="' . check_plain($data) . '"';
  }
  return $attributes ? ' ' . implode(' ', $attributes) : '';
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

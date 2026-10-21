# format_plural()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 1924–1949 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L1924-L1949)
- **Topics:** [format](../../topics/format.md)

## Signature

```php
function format_plural($count, $singular, $plural, array $args = array(), array $options = array())
```

## Documentation

```text
Formats a string containing a count of items.

This function ensures that the string is pluralized correctly. Since t() is
called by this function, make sure not to pass already-localized strings to
it.

For example:
@code
  $output = format_plural($node->comment_count, '1 comment', '@count comments');
@endcode

Example with additional replacements:
@code
  $output = format_plural($update_count,
    'Changed the content type of 1 post from %old-type to %new-type.',
    'Changed the content type of @count posts from %old-type to %new-type.',
    array('%old-type' => $info->old_type, '%new-type' => $info->new_type));
@endcode

@param $count
  The item count to display.
@param $singular
  The string for the singular case. Make sure it is clear this is singular,
  to ease translation (e.g. use "1 new comment" instead of "1 new"). Do not
  use @count in the singular string.
@param $plural
  The string for the plural case. Make sure it is clear this is plural, to
  ease translation. Use @count in place of the item count, as in
  "@count new comments".
@param $args
  An associative array of replacements to make after translation. Instances
  of any key in this array are replaced with the corresponding value.
  Based on the first character of the key, the value is escaped and/or
  themed. See format_string(). Note that you do not need to include @count
  in this array; this replacement is done automatically for the plural case.
@param $options
  An associative array of additional options. See t() for allowed keys.

@return
  A translated string.

@see t()
@see format_string()
```

## Code

```php
function format_plural($count, $singular, $plural, array $args = array(), array $options = array()) {
  $args['@count'] = $count;
  if ($count == 1) {
    return t($singular, $args, $options);
  }

  // Get the plural index through the gettext formula.
  $index = (function_exists('locale_get_plural')) ? locale_get_plural($count, isset($options['langcode']) ? $options['langcode'] : NULL) : -1;
  // If the index cannot be computed, use the plural as a fallback (which
  // allows for most flexiblity with the replaceable @count value).
  if ($index < 0) {
    return t($plural, $args, $options);
  }
  else {
    switch ($index) {
      case "0":
        return t($singular, $args, $options);
      case "1":
        return t($plural, $args, $options);
      default:
        unset($args['@count']);
        $args['@count[' . $index . ']'] = $count;
        return t(strtr($plural, array('@count' => '@count[' . $index . ']')), $args, $options);
    }
  }
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

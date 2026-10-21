# image_style_options()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 791–805 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L791-L805)
- **Module/theme:** image

## Signature

```php
function image_style_options($include_empty = TRUE, $output = CHECK_PLAIN)
```

## Documentation

```text
Gets an array of image styles suitable for using as select list options.

@param $include_empty
  If TRUE a <none> option will be inserted in the options array.
@param $output
  Optional flag determining how the options will be sanitized on output.
  Leave this at the default (CHECK_PLAIN) if you are using the output of
  this function directly in an HTML context, such as for checkbox or radio
  button labels, and do not plan to sanitize it on your own. If using the
  output of this function as select list options (its primary use case), you
  should instead set this flag to PASS_THROUGH to avoid double-escaping of
  the output (the form API sanitizes select list options by default).

@return
  Array of image styles with the machine name as key and the label as value.
```

## Code

```php
function image_style_options($include_empty = TRUE, $output = CHECK_PLAIN) {
  $styles = image_styles();
  $options = array();
  if ($include_empty && !empty($styles)) {
    $options[''] = t('<none>');
  }
  foreach ($styles as $name => $style) {
    $options[$name] = ($output == PASS_THROUGH) ? $style['label'] : check_plain($style['label']);
  }

  if (empty($options)) {
    $options[''] = t('No defined styles');
  }
  return $options;
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._

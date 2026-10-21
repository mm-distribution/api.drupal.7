# php_eval()

- **Type:** Function
- **File:** [`modules/php/php.module`](_file.md), lines 63–88 · [local source](../../../../source/modules/php/php.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/php/php.module#L63-L88)
- **Module/theme:** php
- **Topics:** [php_wrappers](../../../topics/php_wrappers.md)

## Signature

```php
function php_eval($code)
```

## Documentation

```text
Evaluates a string of PHP code.

This is a wrapper around PHP's eval(). It uses output buffering to capture
both returned and printed text. Unlike eval(), we require code to be
surrounded by <?php ?> tags; in other words, we evaluate the code as if it
were a stand-alone PHP file.

Using this wrapper also ensures that the PHP code which is evaluated can not
overwrite any variables in the calling code, unlike a regular eval() call.

This function is also used as an implementation of
callback_filter_process().

@param $code
  The code to evaluate.

@return
  A string containing the printed output of the code, followed by the
  returned output of the code.

@ingroup php_wrappers

@see php_filter_info()
```

## Code

```php
function php_eval($code) {
  global $theme_path, $theme_info, $conf;

  // Store current theme path.
  $old_theme_path = $theme_path;

  // Restore theme_path to the theme, as long as php_eval() executes,
  // so code evaluated will not see the caller module as the current theme.
  // If theme info is not initialized get the path from theme_default.
  if (!isset($theme_info)) {
    $theme_path = drupal_get_path('theme', $conf['theme_default']);
  }
  else {
    $theme_path = dirname($theme_info->filename);
  }

  ob_start();
  print eval('?>' . $code);
  $output = ob_get_contents();
  ob_end_clean();

  // Recover original theme path.
  $theme_path = $old_theme_path;

  return $output;
}
```

---
_Drupal 7.103 · [modules/php/php.module](https://github.com/drupal/drupal/blob/7.103/modules/php/php.module) · Licensed GPL-2.0-or-later (see LICENSE)._

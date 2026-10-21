# openid_redirect()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 90–108 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L90-L108)
- **Module/theme:** openid

## Signature

```php
function openid_redirect($url, $message)
```

## Documentation

```text
Creates a js auto-submit redirect for (for the 2.x protocol)
```

## Code

```php
function openid_redirect($url, $message) {
  global $language;

  $output = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">' . "\n";
  $output .= '<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="' . $language->language . '" lang="' . $language->language . '">' . "\n";
  $output .= "<head>\n";
  $output .= "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />\n";
  $output .= "<title>" . t('OpenID redirect') . "</title>\n";
  $output .= "</head>\n";
  $output .= "<body>\n";
  $elements = drupal_get_form('openid_redirect_form', $url, $message);
  $output .= drupal_render($elements);
  $output .= '<script type="text/javascript">document.getElementById("openid-redirect-form").submit();</script>' . "\n";
  $output .= "</body>\n";
  $output .= "</html>\n";
  print $output;

  drupal_exit();
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

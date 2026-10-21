# openid_extract_ax_values()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 698–715 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L698-L715)
- **Module/theme:** openid

## Signature

```php
function openid_extract_ax_values($values, $uris)
```

## Documentation

```text
Extracts values from an OpenID AX Response.

The values can be returned in two forms:
  - only openid.ax.value.<alias> (for single-valued answers)
  - both openid.ax.count.<alias> and openid.ax.value.<alias>.<count> (for both
    single and multiple-valued answers)

@param $values
  An array as returned by openid_extract_namespace(..., OPENID_NS_AX).
@param $uris
  An array of identifier URIs.
@return
  An array of values.
@see http://openid.net/specs/openid-attribute-exchange-1_0.html#fetch_response
```

## Code

```php
function openid_extract_ax_values($values, $uris) {
  $output = array();
  foreach ($values as $key => $value) {
    if (in_array($value, $uris) && preg_match('/^type\.([^.]+)$/', $key, $matches)) {
      $alias = $matches[1];
      if (isset($values['count.' . $alias])) {
        for ($i = 1; $i <= $values['count.' . $alias]; $i++) {
          $output[] = $values['value.' . $alias . '.' . $i];
        }
      }
      elseif (isset($values['value.' . $alias])) {
        $output[] = $values['value.' . $alias];
      }
      break;
    }
  }
  return $output;
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

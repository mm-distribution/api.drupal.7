# user_category_load()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 2002–2035 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L2002-L2035)
- **Module/theme:** user

## Signature

```php
function user_category_load($uid, &$map, $index)
```

## Documentation

```text
Return a user object after checking if any profile category in the path exists.
```

## Code

```php
function user_category_load($uid, &$map, $index) {
  static $user_categories, $accounts;

  // Cache $account - this load function will get called for each profile tab.
  if (!isset($accounts[$uid])) {
    $accounts[$uid] = user_load($uid);
  }
  $valid = TRUE;
  if ($account = $accounts[$uid]) {
    // Since the path is like user/%/edit/category_name, the category name will
    // be at a position 2 beyond the index corresponding to the % wildcard.
    $category_index = $index + 2;
    // Valid categories may contain slashes, and hence need to be imploded.
    $category_path = implode('/', array_slice($map, $category_index));
    if ($category_path) {
      // Check that the requested category exists.
      $valid = FALSE;
      if (!isset($user_categories)) {
        $user_categories = _user_categories();
      }
      foreach ($user_categories as $category) {
        if ($category['name'] == $category_path) {
          $valid = TRUE;
          // Truncate the map array in case the category name had slashes.
          $map = array_slice($map, 0, $category_index);
          // Assign the imploded category name to the last map element.
          $map[$category_index] = $category_path;
          break;
        }
      }
    }
  }
  return $valid ? $account : FALSE;
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._

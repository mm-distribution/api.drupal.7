# drupal_render_cid_parts()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 6556–6593 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L6556-L6593)

## Signature

```php
function drupal_render_cid_parts($granularity = NULL)
```

## Documentation

```text
Returns cache ID parts for building a cache ID.

@param $granularity
  One or more cache granularity constants. For example, to cache separately
  for each user, use DRUPAL_CACHE_PER_USER. To cache separately for each
  page and role, use the expression:
  @code
  DRUPAL_CACHE_PER_PAGE | DRUPAL_CACHE_PER_ROLE
  @endcode

@return
  An array of cache ID parts, always containing the active theme. If the
  locale module is enabled it also contains the active language. If
  $granularity was passed in, more parts are added.
```

## Code

```php
function drupal_render_cid_parts($granularity = NULL) {
  global $theme, $base_root, $user;

  $cid_parts[] = $theme;
  // If Locale is enabled but we have only one language we do not need it as cid
  // part.
  if (drupal_multilingual()) {
    foreach (language_types_configurable() as $language_type) {
      $cid_parts[] = $GLOBALS[$language_type]->language;
    }
  }

  if (!empty($granularity)) {
    $cache_per_role = $granularity & DRUPAL_CACHE_PER_ROLE;
    $cache_per_user = $granularity & DRUPAL_CACHE_PER_USER;
    // User 1 has special permissions outside of the role system, so when
    // caching per role is requested, it should cache per user instead.
    if ($user->uid == 1 && $cache_per_role) {
      $cache_per_user = TRUE;
      $cache_per_role = FALSE;
    }
    // 'PER_ROLE' and 'PER_USER' are mutually exclusive. 'PER_USER' can be a
    // resource drag for sites with many users, so when a module is being
    // equivocal, we favor the less expensive 'PER_ROLE' pattern.
    if ($cache_per_role) {
      $cid_parts[] = 'r.' . implode(',', array_keys($user->roles));
    }
    elseif ($cache_per_user) {
      $cid_parts[] = "u.$user->uid";
    }

    if ($granularity & DRUPAL_CACHE_PER_PAGE) {
      $cid_parts[] = $base_root . request_uri();
    }
  }

  return $cid_parts;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

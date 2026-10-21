# filter_fallback_format()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 572–580 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L572-L580)
- **Module/theme:** filter

## Signature

```php
function filter_fallback_format()
```

## Documentation

```text
Returns the ID of the fallback text format that all users have access to.

The fallback text format is a regular text format in every respect, except
it does not participate in the filter permission system and cannot be
disabled. It needs to exist because any user who has permission to create
formatted content must always have at least one text format they can use.

Because the fallback format is available to all users, it should always be
configured securely. For example, when the Filter module is installed, this
format is initialized to output plain text. Installation profiles and site
administrators have the freedom to configure it further.

Note that the fallback format is completely distinct from the default format,
which differs per user and is simply the first format which that user has
access to. The default and fallback formats are only guaranteed to be the
same for users who do not have access to any other format; otherwise, the
fallback format's weight determines its placement with respect to the user's
other formats.

Any modules implementing a format deletion functionality must not delete this
format.

@return
  The ID of the fallback text format.

@see hook_filter_format_disable()
@see filter_default_format()
```

## Code

```php
function filter_fallback_format() {
  // This variable is automatically set in the database for all installations
  // of Drupal. In the event that it gets disabled or deleted somehow, there
  // is no safe default to return, since we do not want to risk making an
  // existing (and potentially unsafe) text format on the site automatically
  // available to all users. Returning NULL at least guarantees that this
  // cannot happen.
  return variable_get('filter_fallback_format');
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._

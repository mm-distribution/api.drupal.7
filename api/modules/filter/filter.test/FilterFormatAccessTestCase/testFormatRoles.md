# FilterFormatAccessTestCase::testFormatRoles()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 587–605 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L587-L605)
- **Class:** [FilterFormatAccessTestCase](../FilterFormatAccessTestCase.md)
- **Module/theme:** filter

## Signature

```php
function testFormatRoles()
```

## Documentation

```text
Tests if text format is available to a role.
```

## Code

```php
  function testFormatRoles() {
    // Get the role ID assigned to the regular user; it must be the maximum.
    $rid = max(array_keys($this->web_user->roles));

    // Check that this role appears in the list of roles that have access to an
    // allowed text format, but does not appear in the list of roles that have
    // access to a disallowed text format.
    $this->assertTrue(in_array($rid, array_keys(filter_get_roles_by_format($this->allowed_format))), 'A role which has access to a text format appears in the list of roles that have access to that format.');
    $this->assertFalse(in_array($rid, array_keys(filter_get_roles_by_format($this->disallowed_format))), 'A role which does not have access to a text format does not appear in the list of roles that have access to that format.');

    // Check that the correct text format appears in the list of formats
    // available to that role.
    $this->assertTrue(in_array($this->allowed_format->format, array_keys(filter_get_formats_by_role($rid))), 'A text format which a role has access to appears in the list of formats available to that role.');
    $this->assertFalse(in_array($this->disallowed_format->format, array_keys(filter_get_formats_by_role($rid))), 'A text format which a role does not have access to does not appear in the list of formats available to that role.');

    // Check that the fallback format is always allowed.
    $this->assertEqual(filter_get_roles_by_format(filter_format_load(filter_fallback_format())), user_roles(), 'All roles have access to the fallback format.');
    $this->assertTrue(in_array(filter_fallback_format(), array_keys(filter_get_formats_by_role($rid))), 'The fallback format appears in the list of allowed formats for any role.');
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._

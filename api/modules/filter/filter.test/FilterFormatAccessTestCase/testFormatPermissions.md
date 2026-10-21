# FilterFormatAccessTestCase::testFormatPermissions()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 527–582 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L527-L582)
- **Class:** [FilterFormatAccessTestCase](../FilterFormatAccessTestCase.md)
- **Module/theme:** filter

## Signature

```php
function testFormatPermissions()
```

## Documentation

```text
Tests the Filter format access permissions functionality.
```

## Code

```php
  function testFormatPermissions() {
    // Make sure that a regular user only has access to the text format they
    // were granted access to, as well to the fallback format.
    $this->assertTrue(filter_access($this->allowed_format, $this->web_user), 'A regular user has access to a text format they were granted access to.');
    $this->assertFalse(filter_access($this->disallowed_format, $this->web_user), 'A regular user does not have access to a text format they were not granted access to.');
    $this->assertTrue(filter_access(filter_format_load(filter_fallback_format()), $this->web_user), 'A regular user has access to the fallback format.');

    // Perform similar checks as above, but now against the entire list of
    // available formats for this user.
    $this->assertTrue(in_array($this->allowed_format->format, array_keys(filter_formats($this->web_user))), 'The allowed format appears in the list of available formats for a regular user.');
    $this->assertFalse(in_array($this->disallowed_format->format, array_keys(filter_formats($this->web_user))), 'The disallowed format does not appear in the list of available formats for a regular user.');
    $this->assertTrue(in_array(filter_fallback_format(), array_keys(filter_formats($this->web_user))), 'The fallback format appears in the list of available formats for a regular user.');

    // Make sure that a regular user only has permission to use the format
    // they were granted access to.
    $this->assertTrue(user_access(filter_permission_name($this->allowed_format), $this->web_user), 'A regular user has permission to use the allowed text format.');
    $this->assertFalse(user_access(filter_permission_name($this->disallowed_format), $this->web_user), 'A regular user does not have permission to use the disallowed text format.');

    // Make sure that the allowed format appears on the node form and that
    // the disallowed format does not.
    $this->drupalLogin($this->web_user);
    $this->drupalGet('node/add/page');
    $langcode = LANGUAGE_NONE;
    $elements = $this->xpath('//select[@name=:name]/option', array(
      ':name' => "body[$langcode][0][format]",
      ':option' => $this->allowed_format->format,
    ));
    $options = array();
    foreach ($elements as $element) {
      $options[(string) $element['value']] = $element;
    }
    $this->assertTrue(isset($options[$this->allowed_format->format]), 'The allowed text format appears as an option when adding a new node.');
    $this->assertFalse(isset($options[$this->disallowed_format->format]), 'The disallowed text format does not appear as an option when adding a new node.');
    $this->assertTrue(isset($options[filter_fallback_format()]), 'The fallback format appears as an option when adding a new node.');

    // Check regular user access to the filter tips pages.
    $this->drupalGet('filter/tips/' . $this->allowed_format->format);
    $this->assertResponse(200);
    $this->drupalGet('filter/tips/' . $this->disallowed_format->format);
    $this->assertResponse(403);
    $this->drupalGet('filter/tips/' . filter_fallback_format());
    $this->assertResponse(200);
    $this->drupalGet('filter/tips/invalid-format');
    $this->assertResponse(404);

    // Check admin user access to the filter tips pages.
    $this->drupalLogin($this->admin_user);
    $this->drupalGet('filter/tips/' . $this->allowed_format->format);
    $this->assertResponse(200);
    $this->drupalGet('filter/tips/' . $this->disallowed_format->format);
    $this->assertResponse(200);
    $this->drupalGet('filter/tips/' . filter_fallback_format());
    $this->assertResponse(200);
    $this->drupalGet('filter/tips/invalid-format');
    $this->assertResponse(404);
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._

# PHPAccessTestCase::testNoPrivileges()

- **Type:** Method
- **File:** [`modules/php/php.test`](../_file.md), lines 106–119 · [local source](../../../../../source/modules/php/php.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/php/php.test#L106-L119)
- **Class:** [PHPAccessTestCase](../PHPAccessTestCase.md)
- **Module/theme:** php

## Signature

```php
function testNoPrivileges()
```

## Documentation

```text
Makes sure that the user can't use the PHP filter when not given access.
```

## Code

```php
  function testNoPrivileges() {
    // Create node with PHP filter enabled.
    $web_user = $this->drupalCreateUser(array('access content', 'create page content', 'edit own page content'));
    $this->drupalLogin($web_user);
    $node = $this->createNodeWithCode();

    // Make sure that the PHP code shows up as text.
    $this->drupalGet('node/' . $node->nid);
    $this->assertText('print', 'PHP code was not evaluated.');

    // Make sure that user doesn't have access to filter.
    $this->drupalGet('node/' . $node->nid . '/edit');
    $this->assertNoRaw('<option value="' . $this->php_code_format->format . '">', 'PHP code format not available.');
  }
```

---
_Drupal 7.103 · [modules/php/php.test](https://github.com/drupal/drupal/blob/7.103/modules/php/php.test) · Licensed GPL-2.0-or-later (see LICENSE)._

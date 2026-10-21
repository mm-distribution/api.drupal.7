# PHPFilterTestCase::testPHPFilter()

- **Type:** Method
- **File:** [`modules/php/php.test`](../_file.md), lines 65–88 · [local source](../../../../../source/modules/php/php.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/php/php.test#L65-L88)
- **Class:** [PHPFilterTestCase](../PHPFilterTestCase.md)
- **Module/theme:** php

## Signature

```php
function testPHPFilter()
```

## Documentation

```text
Makes sure that the PHP filter evaluates PHP code when used.
```

## Code

```php
  function testPHPFilter() {
    // Log in as a user with permission to use the PHP code text format.
    $php_code_permission = filter_permission_name(filter_format_load('php_code'));
    $web_user = $this->drupalCreateUser(array('access content', 'create page content', 'edit own page content', $php_code_permission));
    $this->drupalLogin($web_user);

    // Create a node with PHP code in it.
    $node = $this->createNodeWithCode();

    // Make sure that the PHP code shows up as text.
    $this->drupalGet('node/' . $node->nid);
    $this->assertText('print "SimpleTest PHP was executed!"', 'PHP code is displayed.');

    // Change filter to PHP filter and see that PHP code is evaluated.
    $edit = array();
    $langcode = LANGUAGE_NONE;
    $edit["body[$langcode][0][format]"] = $this->php_code_format->format;
    $this->drupalPost('node/' . $node->nid . '/edit', $edit, t('Save'));
    $this->assertRaw(t('Basic page %title has been updated.', array('%title' => $node->title)), 'PHP code filter turned on.');

    // Make sure that the PHP code shows up as text.
    $this->assertNoText('print "SimpleTest PHP was executed!"', "PHP code isn't displayed.");
    $this->assertText('SimpleTest PHP was executed!', 'PHP code has been evaluated.');
  }
```

---
_Drupal 7.103 · [modules/php/php.test](https://github.com/drupal/drupal/blob/7.103/modules/php/php.test) · Licensed GPL-2.0-or-later (see LICENSE)._

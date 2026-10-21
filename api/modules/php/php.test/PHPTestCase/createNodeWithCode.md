# PHPTestCase::createNodeWithCode()

- **Type:** Method
- **File:** [`modules/php/php.test`](../_file.md), lines 45–47 · [local source](../../../../../source/modules/php/php.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/php/php.test#L45-L47)
- **Class:** [PHPTestCase](../PHPTestCase.md)
- **Module/theme:** php

## Signature

```php
function createNodeWithCode()
```

## Documentation

```text
Creates a test node with PHP code in the body.

@return stdObject Node object.
```

## Code

```php
  function createNodeWithCode() {
    return $this->drupalCreateNode(array('body' => array(LANGUAGE_NONE => array(array('value' => '<?php print "SimpleTest PHP was executed!"; ?>')))));
  }
```

---
_Drupal 7.103 · [modules/php/php.test](https://github.com/drupal/drupal/blob/7.103/modules/php/php.test) · Licensed GPL-2.0-or-later (see LICENSE)._

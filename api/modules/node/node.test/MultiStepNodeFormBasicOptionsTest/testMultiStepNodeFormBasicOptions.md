# MultiStepNodeFormBasicOptionsTest::testMultiStepNodeFormBasicOptions()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 2200–2213 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L2200-L2213)
- **Class:** [MultiStepNodeFormBasicOptionsTest](../MultiStepNodeFormBasicOptionsTest.md)
- **Module/theme:** node

## Signature

```php
function testMultiStepNodeFormBasicOptions()
```

## Documentation

```text
Tests changing the default values of basic options to ensure they persist.
```

## Code

```php
  function testMultiStepNodeFormBasicOptions() {
    $edit = array(
      'title' => 'a',
      'status' => FALSE,
      'promote' => FALSE,
      'sticky' => 1,
      'choice[new:0][chtext]' => 'a',
      'choice[new:1][chtext]' => 'a',
    );
    $this->drupalPost('node/add/poll', $edit, t('More choices'));
    $this->assertNoFieldChecked('edit-status', 'status stayed unchecked');
    $this->assertNoFieldChecked('edit-promote', 'promote stayed unchecked');
    $this->assertFieldChecked('edit-sticky', 'sticky stayed checked');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._

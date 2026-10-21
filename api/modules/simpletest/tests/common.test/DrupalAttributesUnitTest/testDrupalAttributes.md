# DrupalAttributesUnitTest::testDrupalAttributes()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 3061–3083 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L3061-L3083)
- **Class:** [DrupalAttributesUnitTest](../DrupalAttributesUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalAttributes()
```

## Documentation

```text
Tests that drupal_html_class() cleans the class name properly.
```

## Code

```php
  function testDrupalAttributes() {
    // Verify that special characters are HTML encoded.
    $this->assertIdentical(drupal_attributes(array('title' => '&"\'<>')), ' title="&amp;&quot;&#039;&lt;&gt;"', 'HTML encode attribute values.');

    // Verify multi-value attributes are concatenated with spaces.
    $attributes = array('class' => array('first', 'last'));
    $this->assertIdentical(drupal_attributes(array('class' => array('first', 'last'))), ' class="first last"', 'Concatenate multi-value attributes.');

    // Verify empty attribute values are rendered.
    $this->assertIdentical(drupal_attributes(array('alt' => '')), ' alt=""', 'Empty attribute value #1.');
    $this->assertIdentical(drupal_attributes(array('alt' => NULL)), ' alt=""', 'Empty attribute value #2.');

    // Verify multiple attributes are rendered.
    $attributes = array(
      'id' => 'id-test',
      'class' => array('first', 'last'),
      'alt' => 'Alternate',
    );
    $this->assertIdentical(drupal_attributes($attributes), ' id="id-test" class="first last" alt="Alternate"', 'Multiple attributes.');

    // Verify empty attributes array is rendered.
    $this->assertIdentical(drupal_attributes(array()), '', 'Empty attributes array.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._

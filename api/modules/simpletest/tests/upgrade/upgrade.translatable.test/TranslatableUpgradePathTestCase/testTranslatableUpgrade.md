# TranslatableUpgradePathTestCase::testTranslatableUpgrade()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.translatable.test`](../_file.md), lines 30–53 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.translatable.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.translatable.test#L30-L53)
- **Class:** [TranslatableUpgradePathTestCase](../TranslatableUpgradePathTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testTranslatableUpgrade()
```

## Documentation

```text
Test a successful upgrade (no negotiation).
```

## Code

```php
  public function testTranslatableUpgrade() {
    if ($this->skipUpgradeTest) {
      return;
    }
    $this->assertTrue($this->performUpgrade(), 'The upgrade was completed successfully.');

    // The D6 database contains the english node "First translatable page" with
    // nid 53.
    $nid = 53;
    $title = 'First translatable page';
    $teaser = 'Teaser of the first translatable page.';
    $body = 'Body of the first translatable page.';

    // Check whether the node displays properly.
    $this->drupalGet("node/$nid");
    $this->assertText($body, 'Translatable node body displays properly');

    // Retrieve node object, ensure that both the body and the teaser has
    // survived upgrade properly.
    $node = $this->drupalGetNodeByTitle($title);
    $this->assertTrue($node != NULL, format_string('Node @title was loaded', array('@title' => $title)));
    $this->assertEqual($node->body[LANGUAGE_NONE][0]['value'], $body, 'Body of the node survived upgrade properly');
    $this->assertEqual($node->body[LANGUAGE_NONE][0]['summary'], $teaser, 'Teaser of the node survived upgrade properly');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.translatable.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.translatable.test) · Licensed GPL-2.0-or-later (see LICENSE)._

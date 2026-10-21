# ForumUpgradePathTestCase::testForumUpgrade()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.forum.test`](../_file.md), lines 29–66 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.forum.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.forum.test#L29-L66)
- **Class:** [ForumUpgradePathTestCase](../ForumUpgradePathTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testForumUpgrade()
```

## Documentation

```text
Test a successful upgrade (no negotiation).
```

## Code

```php
  public function testForumUpgrade() {
    if ($this->skipUpgradeTest) {
      return;
    }
    $this->assertTrue($this->performUpgrade(), 'The upgrade was completed successfully.');

    // Work around http://drupal.org/node/931512
    $this->drupalPost('admin/structure/types/manage/forum/fields', array(), t('Save'));

    // The D6 database forum vocabulary contains the term "Fruits" with id 81.
    $tid = 81;
    $this->drupalGet("forum/$tid");

    // There is one forum topic in Fruits, with the title "Apples".
    $this->clickLink('Apples');
    $this->clickLink('Edit');

    // Add a forum topic "Bananas" to the "Fruits" forum.
    $edit = array(
      'title' => $title = 'Bananas',
      'body[' . LANGUAGE_NONE . '][0][value]' => $body = 'It is another fruit.',
    );
    $this->drupalPost("node/add/forum/$tid", $edit, t('Save'));
    $type = t('Forum topic');
    $this->assertRaw(t('@type %title has been created.', array('@type' => $type, '%title' => $title)), 'Forum topic was created');

    // Retrieve node object, ensure that the topic was created and in the proper forum.
    $node = $this->drupalGetNodeByTitle($title);
    $this->assertTrue($node != NULL, format_string('Node @title was loaded', array('@title' => $title)));
    $this->assertEqual($node->taxonomy_forums[LANGUAGE_NONE][0]['tid'], $tid, 'Saved forum topic was in the expected forum');

    $this->drupalGet("forum/$tid");
    $this->assertText('Bananas');
    $this->drupalLogout();

    $this->drupalGet("node/add/forum/$tid");
    $this->assertResponse(200, 'User can access forum creation page.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.forum.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.forum.test) · Licensed GPL-2.0-or-later (see LICENSE)._

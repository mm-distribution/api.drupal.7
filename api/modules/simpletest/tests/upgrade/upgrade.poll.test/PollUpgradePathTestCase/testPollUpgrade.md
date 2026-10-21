# PollUpgradePathTestCase::testPollUpgrade()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.poll.test`](../_file.md), lines 34–68 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.poll.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.poll.test#L34-L68)
- **Class:** [PollUpgradePathTestCase](../PollUpgradePathTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testPollUpgrade()
```

## Documentation

```text
Test a successful upgrade.
```

## Code

```php
  public function testPollUpgrade() {
    if ($this->skipUpgradeTest) {
      return;
    }
    $this->assertTrue($this->performUpgrade(), 'The upgrade was completed successfully.');

    // Check modules page for poll
    $this->drupalGet('admin/modules');

    // Verify that the poll data is still correctly available
    for ($i = 0; $i < 12; $i++) {
      $this->drupalGet("content/poll/$i");

      $nbchoices = ($i % 4) + 2;

      for ($c = 0; $c < $nbchoices; $c++) {
        $this->assertText("Choice $c for poll $i", 'Choice text is displayed correctly on poll view');
      }

      // Now check that the votes are correct
      $this->clickLink(t('Results'));

      for ($c = 0; $c < $nbchoices; $c++) {
        $this->assertText("Choice $c for poll $i", 'Choice text is displayed correctly on result view');
      }

      $nbvotes = floor (($i % 4) + 5);
      $elements = $this->xpath("//div[@class='percent']");
      for ($c = 0; $c < $nbchoices; $c++) {
        $votes = floor($nbvotes / $nbchoices);
        if (($nbvotes % $nbchoices) > $c) $votes++;
        $this->assertTrue(preg_match("/$votes vote/", $elements[$c]), 'The number of votes is displayed correctly: expected ' . $votes . ', got ' . $elements[$c]);
      }
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.poll.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.poll.test) · Licensed GPL-2.0-or-later (see LICENSE)._

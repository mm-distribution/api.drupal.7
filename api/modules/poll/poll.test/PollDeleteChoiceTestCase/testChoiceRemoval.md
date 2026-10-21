# PollDeleteChoiceTestCase::testChoiceRemoval()

- **Type:** Method
- **File:** [`modules/poll/poll.test`](../_file.md), lines 789–809 · [local source](../../../../../source/modules/poll/poll.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test#L789-L809)
- **Class:** [PollDeleteChoiceTestCase](../PollDeleteChoiceTestCase.md)
- **Module/theme:** poll

## Signature

```php
function testChoiceRemoval()
```

## Documentation

_No docblock in source._

## Code

```php
  function testChoiceRemoval() {
    // Set up a poll with three choices.
    $title = $this->randomName();
    $choices = array('First choice', 'Second choice', 'Third choice');
    $poll_nid = $this->pollCreate($title, $choices, FALSE);
    $this->assertTrue($poll_nid, 'Poll for choice deletion logic test created.');

    // Edit the poll, and try to delete first poll choice.
    $this->drupalGet("node/$poll_nid/edit");
    $edit['choice[chid:1][chtext]'] = '';
    $this->drupalPost(NULL, $edit, t('Save'));

    // Click on the poll title to go to node page.
    $this->drupalGet('poll');
    $this->clickLink($title);

    // Check the first poll choice is deleted, while the others remain.
    $this->assertNoText('First choice', 'First choice removed.');
    $this->assertText('Second choice', 'Second choice remains.');
    $this->assertText('Third choice', 'Third choice remains.');
  }
```

---
_Drupal 7.103 · [modules/poll/poll.test](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test) · Licensed GPL-2.0-or-later (see LICENSE)._

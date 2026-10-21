# PollCreateTestCase::testPollCreate()

- **Type:** Method
- **File:** [`modules/poll/poll.test`](../_file.md), lines 197–236 · [local source](../../../../../source/modules/poll/poll.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test#L197-L236)
- **Class:** [PollCreateTestCase](../PollCreateTestCase.md)
- **Module/theme:** poll

## Signature

```php
function testPollCreate()
```

## Documentation

_No docblock in source._

## Code

```php
  function testPollCreate() {
    $title = $this->randomName();
    $choices = $this->_generateChoices(7);
    $poll_nid = $this->pollCreate($title, $choices, TRUE);

    // Verify poll appears on 'poll' page.
    $this->drupalGet('poll');
    $this->assertText($title, 'Poll appears in poll list.');
    $this->assertText('open', 'Poll is active.');

    // Click on the poll title to go to node page.
    $this->clickLink($title);
    $this->assertText('Total votes: 0', 'Link to poll correct.');

    // Now add a new option to make sure that when we update the node the
    // option is displayed.
    $node = node_load($poll_nid);

    $new_option = $this->randomName();

    $vote_count = '2000';
    $node->choice[] = array(
      'chid' => NULL,
      'chtext' => $new_option,
      'chvotes' => (int) $vote_count,
      'weight' => 1000,
    );

    node_save($node);

    $this->drupalGet('poll');
    $this->clickLink($title);
    $this->assertText($new_option, 'New option found.');

    $option = $this->xpath('//div[@id="node-1"]//div[@class="poll"]//div[@class="text"]');
    $this->assertEqual(end($option), $new_option, 'Last item is equal to new option.');

    $votes = $this->xpath('//div[@id="node-1"]//div[@class="poll"]//div[@class="percent"]');
    $this->assertTrue(strpos(end($votes), $vote_count) > 0, "Votes saved.");
  }
```

---
_Drupal 7.103 · [modules/poll/poll.test](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test) · Licensed GPL-2.0-or-later (see LICENSE)._

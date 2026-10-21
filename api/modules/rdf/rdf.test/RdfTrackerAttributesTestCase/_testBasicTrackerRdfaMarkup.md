# RdfTrackerAttributesTestCase::_testBasicTrackerRdfaMarkup()

- **Type:** Method
- **File:** [`modules/rdf/rdf.test`](../_file.md), lines 625–689 · [local source](../../../../../source/modules/rdf/rdf.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test#L625-L689)
- **Class:** [RdfTrackerAttributesTestCase](../RdfTrackerAttributesTestCase.md)
- **Module/theme:** rdf

## Signature

```php
function _testBasicTrackerRdfaMarkup($node)
```

## Documentation

```text
Helper function for testAttributesInTracker().

Tests the tracker page for RDFa markup.

@param $node
The node just created.
```

## Code

```php
  function _testBasicTrackerRdfaMarkup($node) {
    $url = url('node/' . $node->nid);

    $user = ($node->uid == 0) ? 'Anonymous user' : 'Registered user';

    // Navigate to tracker page.
    $this->drupalGet('tracker');

    // Tests whether the about property is applied. This is implicit in the
    // success of the following tests, but making it explicit will make
    // debugging easier in case of failure.
    $tracker_about = $this->xpath('//tr[@about=:url]', array(':url' => $url));
    $this->assertTrue(!empty($tracker_about), format_string('About attribute found on table row for @user content.', array('@user'=> $user)));

    // Tests whether the title has the correct property attribute.
    $tracker_title = $this->xpath('//tr[@about=:url]/td[@property="dc:title" and @datatype=""]', array(':url' => $url));
    $this->assertTrue(!empty($tracker_title), format_string('Title property attribute found on @user content.', array('@user'=> $user)));

    // Tests whether the relationship between the content and user has been set.
    $tracker_user = $this->xpath('//tr[@about=:url]//td[contains(@rel, "sioc:has_creator")]//*[contains(@typeof, "sioc:UserAccount") and contains(@property, "foaf:name")]', array(':url' => $url));
    $this->assertTrue(!empty($tracker_user), format_string('Typeof and name property attributes found on @user.', array('@user'=> $user)));
    // There should be an about attribute on logged in users and no about
    // attribute for anonymous users.
    $tracker_user = $this->xpath('//tr[@about=:url]//td[@rel="sioc:has_creator"]/*[@about]', array(':url' => $url));
    if ($node->uid == 0) {
      $this->assertTrue(empty($tracker_user), format_string('No about attribute is present on @user.', array('@user'=> $user)));
    }
    elseif ($node->uid > 0) {
      $this->assertTrue(!empty($tracker_user), format_string('About attribute is present on @user.', array('@user'=> $user)));
    }

    // Tests whether the property has been set for number of comments.
    $tracker_replies = $this->xpath('//tr[@about=:url]//td[contains(@property, "sioc:num_replies") and contains(@content, "0") and @datatype="xsd:integer"]', array(':url' => $url));
    $this->assertTrue($tracker_replies, format_string('Num replies property and content attributes found on @user content.', array('@user'=> $user)));

    // Tests that the appropriate RDFa markup to annotate the latest activity
    // date has been added to the tracker output before comments have been
    // posted, meaning the latest activity reflects changes to the node itself.
    $isoDate = date('c', $node->changed);
    $tracker_activity = $this->xpath('//tr[@about=:url]//td[contains(@property, "dc:modified") and contains(@property, "sioc:last_activity_date") and contains(@datatype, "xsd:dateTime") and @content=:date]', array(':url' => $url, ':date' => $isoDate));
    $this->assertTrue(!empty($tracker_activity), format_string('Latest activity date and changed properties found when there are no comments on @user content. Latest activity date content is correct.', array('@user'=> $user)));

    // Tests that the appropriate RDFa markup to annotate the latest activity
    // date has been added to the tracker output after a comment is posted.
    $comment = array(
      'subject' => $this->randomName(),
      'comment_body[' . LANGUAGE_NONE . '][0][value]' => $this->randomName(),
    );
    $this->drupalPost('comment/reply/' . $node->nid, $comment, t('Save'));
    $this->drupalGet('tracker');

    // Tests whether the property has been set for number of comments.
    $tracker_replies = $this->xpath('//tr[@about=:url]//td[contains(@property, "sioc:num_replies") and contains(@content, "1") and @datatype="xsd:integer"]', array(':url' => $url));
    $this->assertTrue($tracker_replies, format_string('Num replies property and content attributes found on @user content.', array('@user'=> $user)));

    // Need to query database directly to obtain last_activity_date because
    // it cannot be accessed via node_load().
    $result = db_query('SELECT t.changed FROM {tracker_node} t WHERE t.nid = (:nid)', array(':nid' => $node->nid));
    foreach ($result as $node) {
      $expected_last_activity_date = $node->changed;
    }
    $isoDate = date('c', $expected_last_activity_date);
    $tracker_activity = $this->xpath('//tr[@about=:url]//td[@property="sioc:last_activity_date" and @datatype="xsd:dateTime" and @content=:date]', array(':url' => $url, ':date' => $isoDate));
    $this->assertTrue(!empty($tracker_activity), format_string('Latest activity date found when there are comments on @user content. Latest activity date content is correct.', array('@user'=> $user)));
  }
```

---
_Drupal 7.103 · [modules/rdf/rdf.test](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test) · Licensed GPL-2.0-or-later (see LICENSE)._

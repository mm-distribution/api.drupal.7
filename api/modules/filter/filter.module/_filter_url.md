# _filter_url()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 1458–1592 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L1458-L1592)
- **Module/theme:** filter
- **Topics:** [standard_filters](../../../topics/standard_filters.md)

## Signature

```php
function _filter_url($text, $filter)
```

## Documentation

```text
Implements callback_filter_process().

Converts text into hyperlinks automatically.

This filter identifies and makes clickable three types of "links".
- URLs like http://example.com.
- E-mail addresses like name@example.com.
- Web addresses without the "http://" protocol defined, like www.example.com.
Each type must be processed separately, as there is no one regular
expression that could possibly match all of the cases in one pass.
```

## Code

```php
function _filter_url($text, $filter) {
  // Tags to skip and not recurse into.
  $ignore_tags = 'a|script|style|code|pre';

  // Pass length to regexp callback.
  _filter_url_trim(NULL, $filter->settings['filter_url_length']);

  // Create an array which contains the regexps for each type of link.
  // The key to the regexp is the name of a function that is used as
  // callback function to process matches of the regexp. The callback function
  // is to return the replacement for the match. The array is used and
  // matching/replacement done below inside some loops.
  $tasks = array();

  // Prepare protocols pattern for absolute URLs.
  // check_url() will replace any bad protocols with HTTP, so we need to support
  // the identical list. While '//' is technically optional for MAILTO only,
  // we cannot cleanly differ between protocols here without hard-coding MAILTO,
  // so '//' is optional for all protocols.
  // @see filter_xss_bad_protocol()
  $protocols = variable_get('filter_allowed_protocols', array('ftp', 'http', 'https', 'irc', 'mailto', 'news', 'nntp', 'rtsp', 'sftp', 'ssh', 'tel', 'telnet', 'webcal'));
  $protocols = implode(':(?://)?|', $protocols) . ':(?://)?';

  // Prepare domain name pattern.
  // The ICANN seems to be on track towards accepting more diverse top level
  // domains (TLDs), so this pattern has been "future-proofed" to allow for
  // TLDs of length 2-64.
  $domain = '(?:[A-Za-z0-9._+-]+\.)?[A-Za-z]{2,64}\b';
  // Mail domains differ from the generic domain pattern, specifically:
  // A . character must be present in the string that follows the @ character.
  $email_domain = '(?:[\p{L}\p{M}\p{N}._+-]+\.)+[\p{L}\p{M}]{2,64}\b';
  $ip = '(?:[0-9]{1,3}\.){3}[0-9]{1,3}';
  $auth = '[a-zA-Z0-9:%_+*~#?&=.,/;-]+@';
  $trail = '[a-zA-Z0-9:%_+*~#&\[\]=/;?!\.,-]*[a-zA-Z0-9:%_+*~#&\[\]=/;-]';

  // Prepare pattern for optional trailing punctuation.
  // Even these characters could have a valid meaning for the URL, such usage is
  // rare compared to using a URL at the end of or within a sentence, so these
  // trailing characters are optionally excluded.
  $punctuation = '[\.,?!]*?';

  // Match absolute URLs.
  $url_pattern = "(?:$auth)?(?:$domain|$ip)/?(?:$trail)?";
  $pattern = "`((?:$protocols)(?:$url_pattern))($punctuation)`";
  $tasks['_filter_url_parse_full_links'] = $pattern;

  // Match e-mail addresses.
  $url_pattern = "[\p{L}\p{M}\p{N}._+-]{1,254}@(?:$email_domain)";
  $pattern = "`($url_pattern)`";
  $tasks['_filter_url_parse_email_links'] = $pattern;

  // Match www domains.
  $url_pattern = "www\.(?:$domain)/?(?:$trail)?";
  $pattern = "`($url_pattern)($punctuation)`";
  $tasks['_filter_url_parse_partial_links'] = $pattern;

  // Each type of URL needs to be processed separately. The text is joined and
  // re-split after each task, since all injected HTML tags must be correctly
  // protected before the next task.
  foreach ($tasks as $task => $pattern) {
    // Store the current text in case any of the preg_* functions fail.
    $saved_text = $text;

    // HTML comments need to be handled separately, as they may contain HTML
    // markup, especially a '>'. Therefore, remove all comment contents and add
    // them back later.
    _filter_url_escape_comments('', TRUE);
    $text = preg_replace_callback('`<!--(.*?)-->`s', '_filter_url_escape_comments', $text);
    if (preg_last_error()) {
      $text = $saved_text;
      continue 1;
    }

    // Split at all tags; ensures that no tags or attributes are processed.
    $chunks = preg_split('/(<.+?>)/is', $text, -1, PREG_SPLIT_DELIM_CAPTURE);
    if (preg_last_error()) {
      $text = $saved_text;
      continue 1;
    }

    // PHP ensures that the array consists of alternating delimiters and
    // literals, and begins and ends with a literal (inserting NULL as
    // required). Therefore, the first chunk is always text:
    $chunk_type = 'text';
    // If a tag of $ignore_tags is found, it is stored in $open_tag and only
    // removed when the closing tag is found. Until the closing tag is found,
    // no replacements are made.
    $open_tag = '';

    for ($i = 0; $i < count($chunks); $i++) {
      if ($chunk_type == 'text') {
        // Only process this text if there are no unclosed $ignore_tags.
        if ($open_tag == '') {
          // If there is a match, inject a link into this chunk via the callback
          // function contained in $task.
          $chunks[$i] = preg_replace_callback($pattern, $task, $chunks[$i]);
          if (preg_last_error()) {
            $text = $saved_text;
            continue 2;
          }
        }
        // Text chunk is done, so next chunk must be a tag.
        $chunk_type = 'tag';
      }
      else {
        // Only process this tag if there are no unclosed $ignore_tags.
        if ($open_tag == '') {
          // Check whether this tag is contained in $ignore_tags.
          if (preg_match("`<($ignore_tags)(?:\s|>)`i", $chunks[$i], $matches)) {
            $open_tag = $matches[1];
          }
        }
        // Otherwise, check whether this is the closing tag for $open_tag.
        else {
          if (preg_match("`<\/$open_tag>`i", $chunks[$i], $matches)) {
            $open_tag = '';
          }
        }
        // Tag chunk is done, so next chunk must be text.
        $chunk_type = 'text';
      }
    }

    $text = implode($chunks);
    // Revert back to the original comment contents
    _filter_url_escape_comments('', FALSE);
    $text = preg_replace_callback('`<!--(.*?)-->`', '_filter_url_escape_comments', $text);
    if (preg_last_error()) {
      $text = $saved_text;
      continue 1;
    }
  }

  return $text;
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._

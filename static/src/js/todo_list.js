$(function() {
  'use strict';

  // リスト選択イベント
  $('.todo-list-table tbody').find('td:not([ignore])').each(function(idx, element) {

    $(element)
      .click(function(e) {
        var $row = $(this).closest('tr'),
            $checkbox = $row.find('.is-done');

        $checkbox.trigger('click');
        return false;
      })
      .find('.is-done')
        .on('click', function(e) {
          var $checkbox = $(this);
          var $parrentRow = $checkbox.closest('tr');
          $parrentRow.attr('data-enabled', $checkbox.is(':checked'));

          $checkbox.promise().done(function() {
            $.ajax({
              'url': '/todo/checked/',
              'type': 'POST',
              'data': {
                'todo_id': $parrentRow.attr('data-id'),
                'is_done': $checkbox.prop('checked') || false
              },
              'dataType': 'json',
              'success': function(response) {return false;}
            });
          });

          // 親要素へのイベント電波を停止
          e.stopPropagation();

        });
  });

});

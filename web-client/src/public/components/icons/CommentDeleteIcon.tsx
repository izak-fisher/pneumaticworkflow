/* eslint-disable max-len */
import * as React from 'react';

export type TCommentDeleteIconProps = React.SVGAttributes<SVGElement>;

export function CommentDeleteIcon({ fill = 'currentColor', ...restProps }: TCommentDeleteIconProps) {
  return (
    <svg width="20" height="20" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" {...restProps}>
      <path
        fillRule="evenodd"
        clipRule="evenodd"
        d="M2 4.99913C2 3.34276 3.34315 2 5 2H15C16.6569 2 18 3.34276 18 4.99913V11.9971C18 13.6535 16.6569 14.9962 15 14.9962H14.1023C13.7592 14.9962 13.4401 15.1721 13.2568 15.4621L12.5365 16.6024C11.3592 18.4659 8.64082 18.4659 7.46353 16.6024L6.74315 15.4621C6.55993 15.1721 6.24078 14.9962 5.89766 14.9962H5C3.34315 14.9962 2 13.6535 2 11.9971V4.99913ZM12.7185 10.3592C13.0938 10.7346 13.0938 11.3431 12.7185 11.7185C12.3431 12.0938 11.7346 12.0938 11.3592 11.7185L10 10.3592L8.64075 11.7185C8.26541 12.0938 7.65685 12.0938 7.28151 11.7185C6.90616 11.3431 6.90616 10.7346 7.28151 10.3592L8.64075 9L7.28151 7.64075C6.90616 7.26541 6.90616 6.65685 7.28151 6.28151C7.65685 5.90616 8.26541 5.90616 8.64075 6.28151L10 7.64075L11.3592 6.28151C11.7346 5.90616 12.3431 5.90616 12.7185 6.28151C13.0938 6.65685 13.0938 7.26541 12.7185 7.64075L11.3592 9L12.7185 10.3592Z"
        fill={fill}
      />
    </svg>
  );
}

class Node {
  // constructor
  constructor(element) {
    this.element = element;
    this.next = null;
  }
}
class LinkedList {
  constructor() {
    this.head = null;
    this.size = 0;
  }

  add(element) {
    // creates a new node
    var node = new Node(element);

    // to store current node
    var current;

    // if list is Empty add the
    // element and make it head
    if (this.head == null) this.head = node;
    else {
      current = this.head;

      // iterate to the end of the
      // list
      while (current.next) {
        current = current.next;
      }

      // add node
      current.next = node;
    }
    this.size++;
  }
  printList() {
    var curr = this.head;
    // var str = "";
    while (curr.next) {
      //str += curr.element + "\n";

      curr = curr.next;
    }
    var output = document.getElementById("contents");

    output.innerHTML = output.innerHTML + "<br>" + curr.element;

    // console.log(str);
  }
}

var ll = new LinkedList();

var socket = io("http://localhost:5000/chat");
socket.on("slackmsg", function (msg) {
  ll.add(msg);
  ll.printList();
  var output = document.getElementById("contents");

  output.scrollTop = output.scrollHeight;
});
socket.on("consolemsg", function (msg) {
  console.log(msg);
  ll.add(msg);
  ll.printList();
  var output = document.getElementById("contents");

  output.scrollTop = output.scrollHeight;
});
document.getElementById("buttonsubmit").onclick = function (e) {
  let msg = document.getElementById("msg").value;
  document.getElementById("msg").value = "";

  // send it to the server
  socket.emit(
    "chat message",
    (json = { from: "console", to: "a-project", msg: msg })
  );

  return false;
};
const input = document.getElementById("upload");
let objectURL;
input.addEventListener("change", function () {
  if (objectURL) {
    // revoke the old object url to avoid using more memory than needed
    URL.revokeObjectURL(objectURL);
  }

  const file = this.files[0];
  objectURL = URL.createObjectURL(file);

  //link.download = file.name; // this name is used when the user downloads the file
  //link.href = objectURL;
  document.getElementById("sendFile").onclick = function (e) {
    socket.emit(
      "send File",
      (json = {
        from: "console",
        to: "a-project",
        filename: file.name,
        objectURL: objectURL,
      })
    );
  };
});

var nameToBeChange = document.getElementById("nameToBeChange");
var listOfPersons = document.getElementById("listOfPersons");
// Change name of the person on clicking any user
var person1 = document.getElementById("person1");
var person2 = document.getElementById("person2");
var person3 = document.getElementById("person3");
var person4 = document.getElementById("person4");
var person5 = document.getElementById("person5");
var person6 = document.getElementById("person6");

const elementsList = document.querySelectorAll(
  "#person1, #person2, #person3, #person4, #person5, #person6"
);
const elementsArray = [...elementsList];

person1.addEventListener("click", function () {
  nameToBeChange.innerHTML = document.getElementById("userName1").innerHTML;

  elementsArray.forEach((element) => {
    element.style.backgroundColor = "#ffffff";
  });

  person1.style.backgroundColor = "#f4f8ff";
});

person2.addEventListener("click", function () {
  nameToBeChange.innerHTML = document.getElementById("userName2").innerHTML;
  elementsArray.forEach((element) => {
    element.style.backgroundColor = "#ffffff";
  });

  listOfPersons.style.backgroundColor = "#ffffff";
  person2.style.backgroundColor = "#f4f8ff";
});

person3.addEventListener("click", function () {
  nameToBeChange.innerHTML = document.getElementById("userName3").innerHTML;
  elementsArray.forEach((element) => {
    element.style.backgroundColor = "#ffffff";
  });

  listOfPersons.style.backgroundColor = "#ffffff";
  person3.style.backgroundColor = "#f4f8ff";
});

person4.addEventListener("click", function () {
  nameToBeChange.innerHTML = document.getElementById("userName4").innerHTML;
  elementsArray.forEach((element) => {
    element.style.backgroundColor = "#ffffff";
  });

  listOfPersons.style.backgroundColor = "#ffffff";
  person4.style.backgroundColor = "#f4f8ff";
});

person5.addEventListener("click", function () {
  nameToBeChange.innerHTML = document.getElementById("userName5").innerHTML;
  elementsArray.forEach((element) => {
    element.style.backgroundColor = "#ffffff";
  });

  listOfPersons.style.backgroundColor = "#ffffff";
  person5.style.backgroundColor = "#f4f8ff";
});

person6.addEventListener("click", function () {
  nameToBeChange.innerHTML = document.getElementById("userName6").innerHTML;
  elementsArray.forEach((element) => {
    element.style.backgroundColor = "#ffffff";
  });

  listOfPersons.style.backgroundColor = "#ffffff";
  person6.style.backgroundColor = "#f4f8ff";
});

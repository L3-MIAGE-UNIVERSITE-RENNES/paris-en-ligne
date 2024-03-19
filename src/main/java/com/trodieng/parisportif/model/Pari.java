package com.trodieng.parisportif.model;

import javax.persistence.*;

import org.openxava.model.*;

import lombok.*;
@Entity @Getter @Setter
public class Pari extends Identifiable  {
	int montant;

}
